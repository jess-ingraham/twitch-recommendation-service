import requests
import json, xml

steamKey = 'B280DA6909B1E40A67ABADB437979FBD'

def getFriends(userID):
    endpoint = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"
    
    parameters = {
        'key' : steamKey,
        'steamid': userID,
        'relationship':'friend',
    }

    resp = requests.get(endpoint, params = parameters)
    
    return resp.json()['friendslist']['friends']

def getOwnedGames(userID):
    endpoint = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    
    parameters = {
        'key' : steamKey,
        'steamid' : userID,
        'include_appinfo' : 1,
        'include_played_free_games' : 1
    }

    resp = requests.get(endpoint, params = parameters)
    
    
    #print(resp.json())
    try:
        games = []
        for game in resp.json()['response']['games']:
            #'name': 'Mini Metro', 'playtime_2weeks': 37, 'playtime_forever': 547
            games.append({'name': game['name'], 'playtime_2weeks': game['playtime_2weeks'],'playtime_forever': game['playtime_forever'] })

        topGames = sorted(games, key = lambda x: x['playtime_forever']) ##sort the games by playtime
        return topGames[:5] #return the top 5

    except KeyError:
        return None



# def getGlobalStats(gameId):
#     endpoint = "http://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v0001/"
    
#     parameters = {
#         'format' : xml,
#         'key' : steamKey,
#         'appId' : gameId,
#         'count' : 1,
#         'name[0]' : 'global.map.emp_isle'
#     }
    
#     resp = requests.get(endpoint, params = parameters)
    
#     return resp.json()


def getUsername(userId):
    endpoint = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    
    parameters = {
        'key' : steamKey,
        'steamids' : userId,
        'personaname' : True
    }

    
    resp = requests.get(endpoint, params = parameters)
    
    return resp.json()['response']['players'][0]['personaname']


def getFinalDict(userId):
    friends = getFriends(userId)
    
    friendList = {}

    for friend in friends:
        username = getUsername(friend['steamid'])
        games = getOwnedGames(friend['steamid'])

        if isinstance(games, list):
            friendList[username] = games
        else: ##skip the user if they have no games
            continue
    return friendList




