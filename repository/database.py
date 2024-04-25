import os
from datetime import date as Date
from typing import Sequence

from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.engine.row import Row
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import subprocess

import configuration
from domain.my_orm import Weather, Precipitate


def run_flyway_migrate(config_file: str):
    command = ["C:/Users/PC/flyway-10.11.1/flyway.cmd", "-configFiles={}".format(config_file), "migrate"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Command executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed with error:")
        print(e.stderr)


def create_session() -> Session:
    load_dotenv()

    if configuration.DATABASE == 'postgresql':
        URL = os.getenv('POSTGRESQL_URL')
        MIGRATE_PATH = os.getenv('POSTGRESQL_MIGRATE_PATH')
    elif configuration.DATABASE == 'mysql':
        URL = os.getenv('MYSQL_URL')
        MIGRATE_PATH = os.getenv('MYSQL_MIGRATE_PATH')
    else:
        raise NameError(f'Invalid database: {configuration.DATABASE}')
    
    run_flyway_migrate(MIGRATE_PATH)
    session = Session(bind=create_engine(URL))

    return session


session = create_session()


def get_weather_informations_by_country_date(country_name: str, date: Date) -> Sequence[Row]:
    statement = (select(Weather.country, Weather.last_updated, Weather.moonrise, Weather.moon_phase)
                 .where((Weather.country == country_name) & (func.date(Weather.last_updated) == date)))
    return session.execute(statement).all()


def get_precipitate_informations_by_country_date(country_name: str, date: Date) -> Sequence[Row]:
    statement = (select(Precipitate.precip_mm, Precipitate.precip_in, Precipitate.humidity, Precipitate.cloud, Precipitate.feels_like_celsius, Precipitate.visibility_km, Precipitate.go_outside_by_weather)
                 .join(Weather, Precipitate.precipitate_id == Weather.weather_id)
                 .where((Weather.country == country_name) & (func.date(Weather.last_updated) == date)))
    return session.execute(statement).all()