
def get_user_input() -> tuple[str, str]:
    country_name = input('Enter country (just name): ')
    date = input('Enter date (appropriate format DD.MM.YYYY): ')

    return country_name, date