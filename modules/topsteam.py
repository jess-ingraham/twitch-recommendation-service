import requests
import json

def getTopGames():
    endpoint = "http://steamspy.com/api.php?request=top100in2weeks"
    resp = requests.get(endpoint)
    
    games = []
    
    for key,value in resp.json().items():
        #average_2weeks = average playtime in the last two weeks. In minutes.
        newdict = {
            'appid': value['appid']
            ,'name':value['name']
            ,'average_hour':value['average_2weeks']/60
            ,'score':value['score_rank']
        }
        games.append(newdict)
        
    top5games = sorted(games, key = lambda x: x['score'])
    
    return top5games[:5]

