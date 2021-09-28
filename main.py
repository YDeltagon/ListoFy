# Import
import spotipy
import json
import PySimpleGUI as SG
import os.path
from spotipy.oauth2 import SpotifyOAuth


# Main windows
def windows_main():
    # Windows to update all
    def windows_update_all():
        # TODO - OAUTH to fix if the TXT files not exist
        def spotify_authentification():
            # Import APP_CLIENT_ID and SECRET
            f_APP_CLIENT_ID = open('APP_CLIENT_ID.txt', 'r')
            APP_CLIENT_ID = f_APP_CLIENT_ID.read()
            f_APP_CLIENT_SECRET = open('APP_CLIENT_SECRET.txt', 'r')
            APP_CLIENT_SECRET = f_APP_CLIENT_SECRET.read()
            APP_CLIENT_LINK = 'http://localhost/'
            APP_CLIENT_SCOPE = 'playlist-read-private user-library-read'
            # Authentification of API
            SPY = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                                                            client_secret=APP_CLIENT_SECRET,
                                                            redirect_uri=APP_CLIENT_LINK,
                                                            scope=APP_CLIENT_SCOPE))
            return SPY

        # All liked track
        def results_all_liked_track(SPY):
            # Parameters
            limit_liked_track = 50
            offset_liked_track = 0
            last_liked_track = False
            old_results_liked_track = SPY.current_user_saved_tracks()
            last_id_liked_track = (old_results_liked_track['total'] - 1)
            file_results_all_liked_track = open("results_all_liked_track.txt", "w")
            file_results_all_liked_track.write('')
            file_results_all_liked_track.close()
            # List of all liked track
            results_all_liked_track = []
            while not last_liked_track:
                file_results_all_liked_track = open("results_all_liked_track.txt", "a")
                for item in SPY.current_user_saved_tracks(limit_liked_track, offset_liked_track)['items']:
                    results_all_liked_track.append(item)
                    file_results_all_liked_track.write(json.dumps(item) + '\n')
                    print(item['added_at'] + ' - ' + item['track']['name'] + ' - ALBUM : ' + item['track']['album'][
                        'name'] + ' - ARTIST : ' + item['track']['artists'][0]['name'] + ' - ID : ' + item['track'][
                              'id'])
                offset_liked_track = offset_liked_track + limit_liked_track
                last_liked_track = (offset_liked_track >= last_id_liked_track)
            file_results_all_liked_track.close()
            return results_all_liked_track

        # All playlist user
        def results_all_playlist_user(sp):
            # Parameters
            last_playlist_user = 'FALSE'
            limit_playlist_user = 50
            offset_playlist_user = 0
            old_results_playlist_user = sp.current_user_playlists()
            last_id_playlist_user = (old_results_playlist_user['total'] - 1)
            # List of all liked track
            results_all_playlist_user = []
            while not last_playlist_user == 'TRUE':
                for item in sp.current_user_playlists(limit_playlist_user, offset_playlist_user)['items']:
                    results_all_playlist_user.append(item)
                    print(item['name'] + ' - ID : ' + item['id'])
                offset_playlist_user = offset_playlist_user + limit_playlist_user
                if offset_playlist_user >= last_id_playlist_user:
                    last_playlist_user = 'TRUE'
            return results_all_playlist_user

        layout = [[SG.Button('Update Spotify info in .txt files'), SG.Exit('Use the .txt files')]]
        window = SG.Window('ListoFy update').Layout(layout)

        while True:
            event, values = window.Read()
            if event in (None, 'Use the .txt files'):
                try:
                    file_results_all_liked_track = open("results_all_liked_track.txt", "r")
                    results_all_liked_track = file_results_all_liked_track.readlines()
                except:
                    print('error')
                break
            if event == 'Update Spotify info in .txt files':
                sp = spotify_authentification()
                results_all_liked_track = results_all_liked_track(sp)
                results_all_playlist_user = results_all_playlist_user(sp)
                break
        window.Close()
        return results_all_playlist_user, results_all_liked_track

    results = windows_update_all()

    file_list_column = [
        [
            # TODO - print all Liked or Playlist on the windows
            SG.Button(button_text="Liked"),
            SG.Button(button_text="Playlist", enable_events=True),
        ],
        [
            SG.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [SG.Text(size=(40, 1), key="-TOUT-")],
        [SG.Image(key="-IMAGE-")],
    ]

    # --  -- - Full layout --  -- -
    layout = [
        [
            SG.Column(file_list_column),
            SG.VSeperator(),
            SG.Column(image_viewer_column),
        ]
    ]

    window = SG.Window("Image Viewer", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == SG.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)

            except:
                pass

    window.close()

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == SG.WIN_CLOSED:
            break

    window.close()


# Reload all infos

windows_main()

"""
last_id_playlist_user = 0
while not last_id_playlist_user == len(results_all_playlist_user):
    print(str(last_id_playlist_user) + ' - ' + results_all_playlist_user[last_id_playlist_user]['name'] + ' - ID : ' + results_all_playlist_user[last_id_playlist_user]['id'])
    last_id_playlist_user = last_id_playlist_user+1 

in_playlist_use_all = input('What playlist numbers do you use for "ALL" ? "none" for no playlist : ')
"""

print('END')
