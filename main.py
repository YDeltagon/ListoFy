### import
import requests
from requests.structures import CaseInsensitiveDict


### Spotify MARKET check
def user_market():
    market_check = ["FR", "EN", "GB"]
    in_user_market = 0
    try: 
        f_user_market = open("user_market.txt", "r")
        in_user_market = f_user_market.read()
        while not in_user_market in market_check:
            in_user_market = input("What is your market ? ")
            if in_user_market in market_check:
                f_save_user_market = input("Save the MARKET on a txt file ? (Y or N)")
                if f_save_user_market == "Y":
                    try:
                        f_user_market = open("user_market.txt", "w")
                        f_user_market.write(in_user_market)
                        f_user_market.close()
                        print("save")
                    except:
                        print("ERROR : The most common error is the missing file, i create one, retry !")
                elif f_save_user_market == "N":
                    print("not save")
                else: 
                    print("WTF ? (not save)")
    except:
        while not in_user_market in market_check:
            in_user_market = input("What is your market ? ")
        f_save_user_market = input("Save the MARKET on a txt file ? (Y or N)")
        if f_save_user_market == "Y":
            try:
                f_user_market = open("user_market.txt", "w")
                f_user_market.write(in_user_market)
                f_user_market.close()
                print("save")
            except:
                print("ERROR : The most common error is the missing file, i create one, retry !")
        elif f_save_user_market == "N":
            print("not save")
        else: 
            print("WTF ? (not save)")
    return in_user_market
        
### Spotify OAUTH check
def user_oauth():
    oauth_verified = 0
    try: 
        f_user_oauth= open("user_oauth.txt", "r")
        in_user_oauth = f_user_oauth.read()
        url = "https://api.spotify.com/v1/me"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer " + in_user_oauth
        if requests.get(url, headers=headers).status_code == 200:
            print('Success !')
            oauth_verified = 1
        elif requests.get(url, headers=headers).status_code == 404:
            print('Not Found.')
        elif requests.get(url, headers=headers).status_code == 401:
            print('Unauthorized.')
        else:
            print('WTF bro ?')
    except:
        while not oauth_verified == 1:
            in_user_oauth = input("What is your OAuth Token ? ")
            url = "https://api.spotify.com/v1/me"
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Content-Type"] = "application/json"
            headers["Authorization"] = "Bearer " + in_user_oauth
            if requests.get(url, headers=headers).status_code == 200:
                print('Success !')
                oauth_verified = 1
            elif requests.get(url, headers=headers).status_code == 404:
                print('Not Found.')
            elif requests.get(url, headers=headers).status_code == 401:
                print('Unauthorized.')
            else:
                print('WTF bro ?')
    return in_user_oauth


### Auth on API Spotify
user_market=user_market()
user_oauth=user_oauth()

print(user_market)
print(user_oauth)