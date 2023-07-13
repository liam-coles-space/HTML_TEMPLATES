from lib.album import Album
#when album object is created it has the correct properties
def test_album_construct():
    album = Album(4, 'Alarm', 1999, 457)
    assert album.id == 4
    assert album.title == 'Alarm'
    assert album.release_year == 1999
    assert album.artist_id == 457

#when str function is called on album object is formats correctly
def test_albums_format_nicely():
    album = Album(1, "Test Title", 1987, 234)
    assert str(album) == "Album(1, Test Title, 1987, 234)"

#when two albums objects have same properties they assert as equal
def test_albums_are_equal():
    album1 = Album(1, "Test Title", 1987, 234)
    album2 = Album(1, "Test Title", 1987, 234)
    assert album1 == album2

def test_album_validity():
    assert Album(None,"","","").is_valid() == False
    assert Album(1,"Title","","").is_valid() == False
    assert Album(1,"Title",1998,"").is_valid() == False
    assert Album(1,"","",2).is_valid() == False
    assert Album(1,"",2080,2).is_valid() == False
    assert Album(1,"Title","",2).is_valid() == False
    assert Album(1,"",2080,"").is_valid() == False
    assert Album(1,None,2080,"").is_valid() == False
    assert Album(1,"Title",None,2).is_valid() == False
    assert Album(1,"Title",2010,None).is_valid() == False
    assert Album(1,"Title",1998,5).is_valid() == True
    assert Album(None,"Title",1998,5).is_valid() == True

def test_album_errors():
    assert Album(None,"","","").generate_errors() == 'Title cannot be blank, Release year cannot be blank, Artist ID cannot be blank'
    assert Album(1,"Title","","").generate_errors() == 'Release year cannot be blank, Artist ID cannot be blank'
    assert Album(1,"Title",1998,"").generate_errors() == 'Artist ID cannot be blank'
    assert Album(1,"","",2).generate_errors() == 'Title cannot be blank, Release year cannot be blank'
    assert Album(1,"",2080,2).generate_errors() == 'Title cannot be blank'
    assert Album(1,"Title","",2).generate_errors() == 'Release year cannot be blank'
    assert Album(1,"",2080,"").generate_errors() == 'Title cannot be blank, Artist ID cannot be blank' 
    assert Album(1,None,2080,"").generate_errors() == 'Title cannot be blank, Artist ID cannot be blank'
    assert Album(1,"Title",None,2).generate_errors() == 'Release year cannot be blank'
    assert Album(1,"Title",2010,None).generate_errors() == 'Artist ID cannot be blank'
    assert Album(1,"Title",1998,5).generate_errors() == None
    assert Album(None,"Title",1998,5).generate_errors() == None


