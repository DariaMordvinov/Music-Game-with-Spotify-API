import random
import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials
from boto.s3.connection import S3Connection

# Gets environment variables (secret token and id)
MY_SPOTIFY_ID = os.environ.get("MY_SPOTIFY_ID")
MY_SECRET = os.environ.get("MY_SECRET")

SP = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=MY_SPOTIFY_ID, client_secret=MY_SECRET))


# Artist class: name, boolean (is this correct answer) and url to their picture
class gameOption:
    def __init__(self, artist, isCorrect, image):
        self.artist = artist
        self.isCorrect = isCorrect
        self.image = image


# Gets the list of artists by genres. I went with this 5 popular ones.
# (Spotify has over 120 genres overall, so we can't choose every genre).
# Can be modified if more/other genres is desired.
def make_artists():
    artists = set()
    result = SP.recommendations(seed_genres=['pop', 'rock', 'blues', 'metal', 'hip-hop'], market='us', limit='10',
                                offset=10)
    for track in result['tracks']:
        for artist in track['artists']:
            id_ = artist['id']
            artists.add(id_)
    return list(artists)


# Function for choosing the track from 20 most populars tracks of the artist
def get_track(artists):
    while True:
        artist = random.choice(artists)
        results = SP.artist_top_tracks(artist)
        track_option = []
        for track in results['tracks'][:20]:
            if track['preview_url'] is not None:
                track_option.append((track['preview_url'], track['name']))

        if len(track_option) > 0:
            track = random.choice(track_option)
            del track_option
            return [track, artist]
        # In case of an error (chosen artist has no tracks to choose from)
        # – start the loop all other again by choosing another artist


# Gets the list of related artists - so we could have some options for the game
def make_options(artist_id):
    similar = SP.artist_related_artists(artist_id)
    others = []
    for artist in similar['artists'][:20]:
        others.append(artist['id'])
    name = SP.artist(artist_id)['name']
    url = SP.artist(artist_id)['images'][0]['url']
    options = [gameOption(name, True, url)]

    while len(options) < 4:
        artist = random.choice(others)
        others.remove(artist)
        options.append(gameOption(SP.artist(artist)['name'], False, SP.artist(artist)['images'][0]['url']))
    del others
    random.shuffle(options)
    return [options, name, url]
