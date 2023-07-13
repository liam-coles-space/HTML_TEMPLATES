from playwright.sync_api import Page, expect, Frame

# Tests for your routes go here

def test_get_albums_html(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    page.goto(f"http://{test_web_address}/albums")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(['Title: Thriller','Release Year: 1982', 'Title: Back In Black', 'Release Year: 1980', 'Title: The Bodyguard', 'Release Year: 1992'])

def test_get_albums_with_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store_extra.sql") # Seed our database with some test data
    page.goto(f"http://{test_web_address}/albums/3")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('The Bodyguard')
    p_tag = page.locator('strong')
    expect(p_tag).to_have_text(['Release year: 1992', 'Artist: Nina Simone'])

def test_get_albums_on_linK(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store_extra.sql") # Seed our database with some test data
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Title: Thriller")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Thriller')
    p_tag = page.locator('strong')
    expect(p_tag).to_have_text(['Release year: 1982', 'Artist: ABBA'])

def test_get_artist_with_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    expect(page).to_have_title('Taylor Swift')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Taylor Swift')
    p_tag = page.locator('p')
    expect(p_tag).to_have_text('Genre: Country')


def test_get_all_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    expect(page).to_have_title('Artists')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Artists')
    p_tag = page.locator('p')
    expect(p_tag).to_have_text(['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone', 'Wild Nothing'])

def test_create_artist_with_form(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=Add a new Artist")
    page.fill("input[name='name']", "The Killers")
    page.fill("input[name='genre']", "Rock")
    page.click("text=Create Artist")
    expect(page).to_have_title('The Killers')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('The Killers')
    p_tag = page.locator('p')
    expect(p_tag).to_have_text('Genre: Rock')

def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=Add a new Artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name cant be blank, Genre cant be blank")

def test_add_album_by_form(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store_extra.sql") # Seed our database with some test data
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Add a new album")
    page.fill("input[name='title']", "test album")

    page.fill("input[name='release_year']", '2007')
    page.fill("input[name='artist_id']", '1')
    page.click("text=Create Album")

    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('test album')
    strong_tag = page.locator('strong')
    expect(strong_tag).to_have_text(['Release year: 2007', 'Artist: Pixies'])


def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_store_extra.sql") # Seed our database with some test data
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("AThere were errors with your submission: Title cannot be blank, Release year cannot be blank, Artist ID cannot be blank")



"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
