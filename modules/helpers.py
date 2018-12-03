import requests
import json

import topsteam as top, SteamFuncs as steam, twitchconn as twitch


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

def getVideosForHomePage():
    topGames= top.getTopGames()
    topGamesList = []
    for game in topGames:
        topGamesList.append(getClips(game['name']))
    return topGamesList

    ## this calls top.getTopGames() which returns an array of dictionaries with
    '''{
        'appid': value['appid']
        ,'name':value['name']
        ,'average_hour':value['average_2weeks']/60
        ,'score':value['score_rank']
    }
    where appID is the steam appId

    take those results and for each game, get the videos from twitch using
    twich.getClips(gameName)
    which returns dictionary with the game name as a key and list of vids as the value

    we want this function to return a list of dictionarys that are returned from getClips
    '''
def getResultsPage(userId):
    allFriends = steam.getFinalDict(userId)
    finalResult = {}

    for friendName, gamesList in allFriends.items():
        for game in gamesList:
            if game['name'] not in finalResult:
                finalResult[game['name']]= {'friends' : [friendName]}
            else:
                finalResult[game['name']]['friends'].append(friendName)

    for game in finalResult.keys():
        finalResult[game]['videos'] = twitch.getClips(game)

    return finalResult






        








