from flask import Flask, render_template
from .helpers import make_options, make_artists, get_track

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    # Gets the list of recommended artists of different genres
    artists = make_artists()

    # Chooses one track of a random artist from the list
    info = get_track(artists)
    track, artist_id = info[0], info[1]
    del info

    # Chooses artists that are similar to the correct answer (by searching for related artists)
    info = make_options(artist_id)
    options, correct, image = info[0], info[1], info[2]
    del info

    # Returns html page with list of artist objects (gameOption), url to the track, correct answer
    # and picture of the correct artist
    return render_template('index.html', options=options, track=track, correct=correct, image=image)
