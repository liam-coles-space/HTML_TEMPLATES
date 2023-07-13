import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('new_album.html')


@app.route('/albums', methods = ['POST'])
def create_album():
    print('horse')
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    if not album.is_valid():
        print (album.generate_errors())
        return render_template('new_album.html', album=album, errors=album.generate_errors()), 400
    
    album_id = repository.add(album.title, album.release_year, album.artist_id)
    print('im here')
    return redirect(f"/albums/{album_id}")

    

@app.route('/albums/<id>', methods=['GET'])
def get_albums_id(id):
    connection = get_flask_database_connection(app)      
    repository = AlbumRepository(connection)
    album_and_artist = repository.find_with_artist(id)
    album = album_and_artist[0]
    artist = album_and_artist[1]
    return render_template('album_with_artist.html', album=album, artist=artist)

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)      
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)

@app.route('/artists/new', methods=['GET'])
def get_new_artist_form():
    return render_template('new_artist.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)

    if not artist.is_valid():
        print (artist.generate_errors())
        return render_template('new_artist.html', artist=artist, errors=artist.generate_errors()), 400
    
    artist_id = repository.add(artist.name, artist.genre)

    return redirect(f"/artists/{artist_id}")

@app.route('/artists/<id>', methods=['GET'])
def get_artist_by_id(id):
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artist.html', artist=artist)

@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app) 
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists.html', artists=artists)


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
