import os
import pandas as pd

def create_table_populate_sql(path=''):
    if path:
        os.chdir(path)

    df = pd.read_csv('table_creation\GlobalWeatherRepository.csv')
    df = df[['country', 'precip_mm', 'precip_in', 'humidity', 'cloud', 'feels_like_celsius', 
             'visibility_km', 'last_updated', 'moonrise', 'moon_phase']]

    df = df[df['moonrise'] != 'No moonrise']
    df['moonrise'] = df['moonrise'].map(lambda x: x[:-3])

    table_creation_query = '''INSERT INTO weather_informations (country, precip_mm, precip_in, humidity, 
                           cloud, feels_like_celsius, visibility_km, last_updated, moonrise, moon_phase) VALUES '''

    with open('table_creation\\table_population.sql', 'w', encoding='UTF-8') as file:
        for i, row in df.iterrows():
            query = table_creation_query + str(tuple(row)) + ';\n'
            file.write(query)


if __name__ == '__main__':
    create_table_populate_sql()
