# Music Game

#### This is a simple Flask application with Spotify API 

There is a 30-second song sample on the main page. User has to guess who plays the song. There are four options to choose from.
User makes his choice by clicking on one of the options. The game will show the correct answer and say if the user was right. 

[Video Demo](https://youtu.be/CD0t5YVBrGc)

To run this application you'll need Flask, spopipy python library, Bootstrap, JQuery and dotenv (for retrieving API key from the environment). You'll also need Spotify
Client ID and Client Secret. You can find those on Spotify for developers Dashbord.

## How it works

#### helpers.py

1) Firstly, the app gets recommendations of tracks on several genres. I chose 'rock', 'metal', 'pop', 'blues' and 'hip-hop'. You can choose whatever genres you like, 
but I don't recommend choosing anything too specific – otherwise it won't cover many artists. There are more then 120 genres on Spotify and remember, accodring to Spotify 
documentation you may provide up to 5 seed values in one single request on recommendation. 
I figured these 5 broad genres would be enough for my demo-version. They provide good variety of options. With this list of recommended tracks I make a list of recommended artists.

2) Then the app randomly chooses one artist among the list. With another request, you can get artist's top tracks. App choses one of the tracks randomly and save this information.

3) For storing information on artist I created a new class – gameOption with 'artist', 'isCorrect' and 'image' properties. In the 'isCorrect' property I'm going to store boolean value.
If the artist is the author of the playing track, the value is True.

4) With the next step app requests the list of "related" artists (artist that Spotify considers similar to the author of the track). 
We need another 3 artists so there could be 4 options to choose from.

##### application.py

We'll need only one route, the index one. When user opens the website, the app retrieves all the data for the game and renderes the template with the several values 
(list of options, correct answer and the track).
