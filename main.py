### import
import json
import requests
from requests.structures import CaseInsensitiveDict
from requests.exceptions import HTTPError

### Auth on API Spotify
in_user_market = input("What is your market ? (FR/EN/IT...) ")
in_user_oauth = input("What is your OAuth Token ? ")
url = f"https://api.spotify.com/v1/me/tracks?offset=0&limit=50&market={in_user_market}"

### Give like track/artist/album on Spotify
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {in_user_oauth}"

### 
resp = requests.get(url, headers=headers)

### print status code
print(resp)

### Succes or not
if resp.status_code == 200:
    print('Success !')
elif resp.status_code == 404:
    print('Not Found.')
elif resp.status_code == 401:
    print('Unauthorized.')
else:
    print('WTF bro ?')