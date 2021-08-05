
#* Import
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#* Import APP_CLIENT_ID and SECRET
f_APP_CLIENT_ID = open("APP_CLIENT_ID.txt", "r")
APP_CLIENT_ID = f_APP_CLIENT_ID.read()
f_APP_CLIENT_SECRET = open("APP_CLIENT_SECRET.txt", "r")
APP_CLIENT_SECRET = f_APP_CLIENT_SECRET.read()

#* Authentification
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                                               client_secret=APP_CLIENT_SECRET,
                                               redirect_uri="http://localhost/",
                                               scope="user-library-read"))

#* Parametres
last_liked_track = "FALSE"
limit_liked_track = 50
offset_liked_track = 0
old_liked_track_results = sp.current_user_saved_tracks()
last_liked_track_id = (old_liked_track_results['total']-1)
total_liked_track = (old_liked_track_results['total'])

#* List of all liked track
results = []
while not last_liked_track == "TRUE" :
    for item in sp.current_user_saved_tracks(limit_liked_track, offset_liked_track)['items']:
        results.append(item['track'])
    offset_liked_track = offset_liked_track + limit_liked_track
    if offset_liked_track >= last_liked_track_id:
        last_liked_track = "TRUE"

#* Total of all liked track
print("total : " + str(total_liked_track))
