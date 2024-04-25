from typing import Sequence
from sqlalchemy.engine.row import Row
from tabulate import tabulate


def show_informations(weather_informations: Sequence[Row], precipitate_informations: Sequence[Row]) -> None:
    print('\n' + 'Weather')
    print(tabulate(weather_informations, ('Country', 'Last Updated', 'Moonrise', 'Moon_phase'), tablefmt='pretty'))

    print('\n' + 'Precipitate')
    print(tabulate(precipitate_informations, ('Precipitate (mm)', 'Precipitate (in)', 'Humidity', 'Cloude', 'Feels like celsius', 'Visibility (km)', 'Go outside by weather?'), tablefmt='pretty'))