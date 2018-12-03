#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
import json


# In[20]:


clientID= 'dcu07oqpaghxhvrwpf7rz85qxzqkik'
headers = {'Client-ID':clientID}


# In[51]:


def getClips(gameName):
    
    endpoint = f'https://api.twitch.tv/helix/games?name={gameName}'
    resp = requests.get(endpoint, headers=headers)
    gameID= resp.json()['data'][0]['id']
    results= __getVideoInfo(gameID)
    return results


# In[52]:


def __getVideoInfo(gameID):
    endpoint = f'https://api.twitch.tv/helix/videos?game_id={gameID}&sort=views&first=5&language=en'
    resp = requests.get(endpoint, headers=headers)
    videos = []
    for video in resp.json()['data']:
        dictionary = {
            'id': video['id'],
            'title': video['title'],
            'username': video['user_name'],
            'view_count':video['view_count']
        }
        videos.append(dictionary)
    return videos


# In[53]:


test= getClips('Stardew Valley')
test


# In[ ]:


#<iframe src="https://player.twitch.tv/?autoplay=false&video=v341081301" frameborder="0" allowfullscreen="true" scrolling="no" height="378" width="620"></iframe><a href="https://www.twitch.tv/videos/341081301?tt_content=text_link&tt_medium=vod_embed" style="padding:2px 0px 4px; display:block; width:345px; font-weight:normal; font-size:10px; text-decoration:underline;"></a>

