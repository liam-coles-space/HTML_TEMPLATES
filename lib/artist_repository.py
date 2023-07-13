from lib.artist import Artist 

class ArtistRepository:
    # Attributes:
    #   connection: db_connection object
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        # SQL used: 
        #   SELECT id, name, genre FROM artists
        # Returns:
        #   A list of Artist Objects
        rows = self._connection.execute('SELECT id, name, genre FROM artists')
        albums = []
        for row in rows:
            albums.append(Artist(row['id'],row['name'], row['genre']))

        
        return albums

    def add(self, name, genre):
        #SQL used:
        #   INSERT INTO artists(name, genre) values(name,genre)
        self._connection.execute('INSERT INTO artists(name, genre) values(%s,%s)', [name, genre])

    def find(self, artist_id):
        rows = self._connection.execute('SELECT id, name, genre FROM artists WHERE id = %s', [artist_id])
        return Artist(rows[0]['id'], rows[0]['name'], rows[0]['genre'])
    