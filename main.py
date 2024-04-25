from datetime import datetime

from present_result.user_input import get_user_input
from present_result.result_output import show_informations
from service.get_precipitate_information import get_weather_precipitate_informations


if __name__ == '__main__':
    country_name, date = get_user_input()

    data = date = datetime.strptime(date, '%d.%m.%Y').date()
    weather_data, wind_data = get_weather_precipitate_informations(country_name, date)

    show_informations(weather_data, wind_data)