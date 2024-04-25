CREATE TABLE precipitate_informations(
    precipitate_id     serial PRIMARY KEY REFERENCES weather_informations(weather_id),
    precip_mm          real NOT NULL,
    precip_in          real NOT NULL,
    humidity           int NOT NULL,
    cloud              int NOT NULL,
    feels_like_celsius real NOT NULL,
    visibility_km      real NOT NULL
);

INSERT INTO precipitate_informations 
SELECT weather_id, precip_mm, precip_in, humidity, cloud, feels_like_celsius, visibility_km
FROM weather_informations;

ALTER TABLE weather_informations DROP COLUMN precip_mm,
                                 DROP COLUMN precip_in,
                                 DROP COLUMN humidity,
                                 DROP COLUMN cloud,
                                 DROP COLUMN feels_like_celsius,
                                 DROP COLUMN visibility_km;