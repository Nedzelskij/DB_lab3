from sqlalchemy import Column, Integer, String, Enum, Float, DateTime, Time, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather_informations'

    weather_id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    last_updated = Column(DateTime, nullable=False)
    moonrise = Column(Time, nullable=False)
    moon_phase = Column(Enum('Waning Gibbous', 'Waxing Gibbous', 'Waxing Crescent', 'Waning Crescent', 'Full Moon', 'New Moon', 'Last Quarter', 'First Quarter'), nullable=False)


class Precipitate(Base):
    __tablename__ = 'precipitate_informations'

    precipitate_id = Column(Integer, ForeignKey('weather_informations.weather_id'), primary_key=True)
    precip_mm = Column(Float, nullable=False)
    precip_in = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    cloud = Column(Integer, nullable=False)
    feels_like_celsius = Column(Float, nullable=False)
    visibility_km = Column(Float, nullable=False)
    go_outside_by_weather = Column(Boolean, nullable=False)