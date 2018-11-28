import requests
import json


def __getUserId(vanityUrl):
    endpoint = f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&vanityurl={vanityUrl}'
    
    resp = requests.get(endpoint)
    print(resp.json())
    try:
        if resp.json()['response']['success'] == 42:
            return 42
        else:
            return resp.json()['response']['steamid']
    except KeyError:
        return 4 ##bad request
    
    return resp.json()
    

def checkURL(url):
    parts = url.split('/')
    if(parts[2] != 'steamcommunity.com'):
        return 3 ##something wrong with url
    try:
        s_id = parts[4]
        int(s_id)
        return s_id
    except ValueError:
        vanity = s_id
        s_id = __getUserId(vanity)
        return s_id
    except:
        return 3 ##something wrong with the url




