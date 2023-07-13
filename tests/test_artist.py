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

def test_artist_validity():
    assert Artist(5, None, 'Pop').is_valid() == False
    assert Artist(5, 'Monkeys', None).is_valid() == False
    assert Artist(5, None, None).is_valid() == False
    assert Artist(5, 'Monkeys', '').is_valid() == False
    assert Artist(5, '', 'Pop').is_valid() == False
    assert Artist(5, '', '').is_valid() == False
    assert Artist(None , 'Monkeys', 'Pop').is_valid() == True
    assert Artist(4 , 'Monkeys', 'Pop').is_valid() == True

def test_artist_errors():
    assert Artist(5, None, 'Pop').generate_errors() == 'Name cant be blank'
    assert Artist(5, 'Monkeys', None).generate_errors() == 'Genre cant be blank'
    assert Artist(5, None, None).generate_errors() == 'Name cant be blank, Genre cant be blank'
    assert Artist(5, 'Monkeys', '').generate_errors() == 'Genre cant be blank'
    assert Artist(5, '', 'Pop').generate_errors() == 'Name cant be blank'
    assert Artist(5, '', '').generate_errors() == 'Name cant be blank, Genre cant be blank'
    assert Artist(None , 'Monkeys', 'Pop').generate_errors() == None
    assert Artist(4 , 'Monkeys', 'Pop').generate_errors() == None 