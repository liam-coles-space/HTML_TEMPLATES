from lib.album import *
from lib.artist import *
class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection 

#Get all albums stored in the albums table as a list
    def all(self):
    # Sql Used:
    #   SELECT id, title, release_year, artist_id FROM albums
    # Returns:
        #list of Album objects
        rows = self._connection.execute('SELECT id, title, release_year, artist_id FROM albums')
        albums = []
        for row in rows:
            albums.append(Album(row['id'], row['title'], row['release_year'], row['artist_id']))
        return albums
    
    


#add new album to albums table 
    def add(self,title, release_year, artist_id):
    # Parameters:
    #   title: string
    #   release_year: int
    #   artist_id: int
    # Side effects:
    #   Adds record to album table
    # Sql used:
    #   INSERT INTO albums(title, release_year, artist_id) VALUES(%s,%s,%s)
        rows = self._connection.execute('INSERT INTO albums(title, release_year, artist_id) VALUES(%s,%s,%s) RETURNING ID', [title, release_year, artist_id])
        print(rows)
        row = rows[0]
        return row['id']


    
    def find_with_artist(self, id):
        rows = self._connection.execute('SELECT albums.id as album_id, title, release_year, artists.id as artist_id, name, genre from albums join artists on albums.artist_id = artists.id where albums.id = %s', [id])
        return_objects = []
        return_objects.append(Album(rows[0]['album_id'], rows[0]['title'], rows[0]['release_year'],rows[0]['artist_id']))
        return_objects.append(Artist(rows[0]['artist_id'], rows[0]['name'], rows[0]['genre']))
        return return_objects


