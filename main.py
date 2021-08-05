import spotipy
from spotipy.oauth2 import SpotifyOAuth

f_APP_CLIENT_ID = open("APP_CLIENT_ID.txt", "r")
APP_CLIENT_ID = f_APP_CLIENT_ID.read()
f_APP_CLIENT_SECRET = open("APP_CLIENT_SECRET.txt", "r")
APP_CLIENT_SECRET = f_APP_CLIENT_SECRET.read()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                                               client_secret=APP_CLIENT_SECRET,
                                               redirect_uri="http://localhost/",
                                               scope="user-library-read"))

last_track = 0
limit = 50
offset = 0
results = sp.current_user_saved_tracks()
total_song = (results['total']-1)
print("total : " + str(total_song))
while not last_track == 1 :
    results = sp.current_user_saved_tracks(limit, offset)

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(offset + idx, track['artists'][0]['name'], " – ", track['name'])

    offset = offset + limit
    if offset >= total_song:
        last_track = 1

print("total : " + str(total_song))