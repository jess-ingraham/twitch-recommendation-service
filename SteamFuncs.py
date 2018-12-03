import requests
import json, xml

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
    
    try:
        return resp.json()['response']['games']
    except:
        return("Not available.")


def getGlobalStats(gameId):
    endpoint = "http://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v0001/"
    
    parameters = {
        'format' : xml,
        'key' : steamKey,
        'appId' : gameId,
        'count' : 1,
        'name[0]' : 'global.map.emp_isle'
    }
    
    resp = requests.get(endpoint, params = parameters)
    
    return resp.json()


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
        friendList[username] = getOwnedGames(friend['steamid'])
        if isinstance(getOwnedGames(friend['steamid']),list):
            for i in range(len(getOwnedGames(friend['steamid']))):
                del friendList[username][i]['appid']
                del friendList[username][i]['img_icon_url']
                del friendList[username][i]['img_logo_url']

    
                
    return friendList




