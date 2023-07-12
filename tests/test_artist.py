from lib.artist import Artist
#when Artist object is created it initializes with the correct properties
def test_artist_construct():
    artist = Artist(5, 'Monkeys', 'Pop')
    assert artist.id == 5
    assert artist.name == 'Monkeys'
    assert artist.genre == 'Pop'

#when str function is called on Artist object it formats correctly
def test_artists_format_nicely():
    artist = Artist(5, 'Monkeys', 'Pop')
    assert str(artist) == "Artist(5, Monkeys, Pop)"

#when two Artist objects have same properties they assert as equal
def test_two_objects_match():
    artist1 = Artist(5, 'Monkeys', 'Pop')
    artist2 = Artist(5, 'Monkeys', 'Pop')
    assert artist1 == artist2
