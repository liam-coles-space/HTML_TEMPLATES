DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO albums(title, release_year, artist_id) values
    ('Thriller', 1982, 2), 
    ('Back In Black', 1980, 3),
    ('The Bodyguard', 1992, 4);

INSERT INTO artists(name, genre) values
    ('Pixies', 'Grunge'),
    ('ABBA', 'Pop'),
    ('Taylor Swift', 'Country'),
    ('Nina Simone', 'Blues'),
    ('Wild Nothing', 'Rock')
    