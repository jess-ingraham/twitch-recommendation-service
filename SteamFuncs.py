#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json, xml


# In[2]:


def getFriends(userID):
    endpoint = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"
    
    parameters = {
        'key' : steamKey,
        'steamid': userID,
        'relationship':'friend',
    }

    resp = requests.get(endpoint, params = parameters)
    
    return resp.json()['friendslist']['friends']


# In[3]:


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


# In[4]:


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


# In[5]:


def getUsername(userId):
    endpoint = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    
    parameters = {
        'key' : steamKey,
        'steamids' : userId,
        'personaname' : True
    }

    
    resp = requests.get(endpoint, params = parameters)
    
    return resp.json()['response']['players'][0]['personaname']


# In[ ]:




