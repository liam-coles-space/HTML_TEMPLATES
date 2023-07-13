from lib.artist import Artist
from lib.artist_repository import ArtistRepository
#when all method is called a list of Artist objects are returned, with each objects properties representing the data of a record from the artists table, with an object per record

def test_all_records_returned(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new BookRepository
    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Grunge'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Country'),
        Artist(4, 'Nina Simone', 'Blues'),
        Artist(5, 'Wild Nothing', 'Rock'),
    ]

#when add method is called a new record is created in the artists table with the data passed into the add method
def test_add_creates_record(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new BookRepository
    artist_id = repository.add('Bloc Party', 'Indie')
    assert artist_id == 6
    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Grunge'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Country'),
        Artist(4, 'Nina Simone', 'Blues'),
        Artist(5, 'Wild Nothing', 'Rock'),
        Artist(6, 'Bloc Party', 'Indie'),
    ]

"""
call find artist by id
returns artist object 
"""
def test_find_artist(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection)
    artist = repository.find(3)
    assert artist == Artist(3, 'Taylor Swift', 'Country')
