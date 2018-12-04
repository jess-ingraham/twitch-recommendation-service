import requests
import json

from modules import topsteam as top, SteamFuncs as steam, twitchconn as twitch


def __getUserId(vanityUrl):
    endpoint = f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&vanityurl={vanityUrl}'
    
    resp = requests.get(endpoint)
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
    topGamesList = {}
    count = 0

    while (len(topGamesList) < 5):
        ##if there are no videos returned for that game, we skip it and go to the next game
        game = topGames[count]
        clips = twitch.getClips(game['name'])

        if clips != None:
            topGamesList[game['name']] = {'videos': clips}
            count += 1
        else:
            count += 1
            continue

    return topGamesList


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

    return (steam.getUsername(userId), finalResult)






        








