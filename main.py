
#* Import
import spotipy
import time
from fileinput import close
from spotipy.oauth2 import SpotifyOAuth

#* Import APP_CLIENT_ID and SECRET
f_APP_CLIENT_ID = open('APP_CLIENT_ID.txt', 'r')
APP_CLIENT_ID = f_APP_CLIENT_ID.read()
f_APP_CLIENT_ID = close
f_APP_CLIENT_SECRET = open('APP_CLIENT_SECRET.txt', 'r')
APP_CLIENT_SECRET = f_APP_CLIENT_SECRET.read()
f_APP_CLIENT_SECRET = close

#* All liked track
def results_all_liked_track(client_id, client_secret):
    #* Authentification
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = client_id, 
                                                client_secret = client_secret, 
                                                redirect_uri = 'http://localhost/', 
                                                scope = 'user-library-read'))

    #* Parametres
    last_liked_track = 'FALSE'
    limit_liked_track = 50
    offset_liked_track = 0
    old_results_liked_track = sp.current_user_saved_tracks()
    last_id_liked_track = (old_results_liked_track['total']-1)

    #* List of all liked track
    results_all_liked_track = []
    while not last_liked_track == 'TRUE' :
        for item in sp.current_user_saved_tracks(limit_liked_track, offset_liked_track)['items']:
            results_all_liked_track.append(item)
            print(item['added_at'] + ' - ' + item['track']['name'] + ' - ALBUM : ' + item['track']['album']['name'] + ' - ARTIST : ' + item['track']['artists'][0]['name'] + ' - ID : ' + item['track']['id'])
        offset_liked_track = offset_liked_track + limit_liked_track
        if offset_liked_track >= last_id_liked_track:
            last_liked_track = 'TRUE'

    return results_all_liked_track


#* All playlist user
def results_all_playlist_user(client_id, client_secret):
    #* Authentification
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = client_id, 
                                                client_secret = client_secret, 
                                                redirect_uri = 'http://localhost/', 
                                                scope = 'playlist-read-private'))

    #* Parametres
    last_playlist_user = 'FALSE'
    limit_playlist_user = 50
    offset_playlist_user = 0
    old_results_playlist_user = sp.current_user_playlists()
    last_id_playlist_user = (old_results_playlist_user['total']-1)

    #* List of all liked track
    results_all_playlist_user = []
    while not last_playlist_user == 'TRUE' :
        for item in sp.current_user_playlists(limit_playlist_user, offset_playlist_user)['items']:
            results_all_playlist_user.append(item)
            print(item['name'] + ' - ID : ' + item['id'])
        offset_playlist_user = offset_playlist_user + limit_playlist_user
        if offset_playlist_user >= last_id_playlist_user:
            last_playlist_user = 'TRUE'

    return results_all_playlist_user


#* 
results_all_liked_track=results_all_liked_track(APP_CLIENT_ID, APP_CLIENT_SECRET)
results_all_playlist_user = results_all_playlist_user(APP_CLIENT_ID, APP_CLIENT_SECRET)

#? A question to chose a "All" Playlist
''' last_id_playlist_user = 0
while not last_id_playlist_user == len(results_all_playlist_user):
    print(str(last_id_playlist_user) + ' - ' + results_all_playlist_user[last_id_playlist_user]['name'] + ' - ID : ' + results_all_playlist_user[last_id_playlist_user]['id'])
    last_id_playlist_user = last_id_playlist_user+1

in_playlist_use_all = input('What playlist numbers do you use for "ALL" ? "none" for no playlist : ') '''

print('END')

