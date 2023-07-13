from playwright.sync_api import Page, expect, Frame

# Tests for your routes go here

# === Example Code Below ===

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
