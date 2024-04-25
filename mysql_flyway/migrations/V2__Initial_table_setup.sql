CREATE TABLE weather_informations(
    weather_id         serial PRIMARY KEY,
    country            varchar(40) NOT NULL,
    precip_mm          real NOT NULL,
    precip_in          real NOT NULL,
    humidity           int NOT NULL,
    cloud              int NOT NULL,
    feels_like_celsius real NOT NULL,
    visibility_km      real NOT NULL,
    last_updated       timestamp NOT NULL,
    moonrise           time NOT NULL,
    moon_phase         ENUM('Waning Gibbous', 'Waxing Gibbous', 'Waxing Crescent', 'Waning Crescent', 'Full Moon', 'New Moon', 'Last Quarter', 'First Quarter') NOT NULL
);