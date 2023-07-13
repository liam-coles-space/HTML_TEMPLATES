from lib.album import Album
from lib.artist import Artist
from lib.album_repository import AlbumRepository

#when all method is called i get a list of album objects back that represents all records in the albums table
def test_all_returns_records(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        Album(1, "Thriller", 1982, 19),
        Album(2, "Back In Black", 1980, 345),
        Album(3, "The Bodyguard", 1992, 32),
    ]


#when add methods is called a new record is added to the albums table whose data matches the arguements passed into the method
def test_add_method(db_connection):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository

    album_id = repository.add('Silent Alarm', 2008, 784)
    assert album_id == 4

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        Album(1, "Thriller", 1982, 19),
        Album(2, "Back In Black", 1980, 345),
        Album(3, "The Bodyguard", 1992, 32),
        Album(4, "Silent Alarm", 2008, 784),
    ]

def test_find_album_with_artist(db_connection):
    db_connection.seed("seeds/music_store_extra.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository
    rows = repository.find_with_artist(3)
    assert rows == [
        Album(3, 'The Bodyguard', 1992, 4),
        Artist(4, 'Nina Simone', 'Blues')
    ]
    
