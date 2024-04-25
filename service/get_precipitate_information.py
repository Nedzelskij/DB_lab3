from datetime import datetime
from typing import Sequence
from sqlalchemy.engine.row import Row
from repository.database import get_weather_informations_by_country_date, get_precipitate_informations_by_country_date

def get_weather_precipitate_informations(country_name: str, date: datetime.date) -> tuple[Sequence[Row], Sequence[Row]]:
    
    return get_weather_informations_by_country_date(country_name, date), get_precipitate_informations_by_country_date(country_name, date)