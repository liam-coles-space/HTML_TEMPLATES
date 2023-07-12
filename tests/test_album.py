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


