#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 01:00:21 2019

@author: liuyang
"""

import requests
import json

def get_tweets(year):
    #  the truly excellent Trump Twitter Archive, which contains all of Trump’s tweets going back to 2009.
    url = ('http://www.trumptwitterarchive.com/data/realdonaldtrump/%s.json' %year)
    r = requests.get(url)
    print(str(year) + ' --> ' + 'done.')
    return r.json()

def save_tweets(years=range(2010,2019)):
        
        tweets = []
        for y in years:
            data = get_tweets(y)
            dl = len(data)
            
            i = 0
            while i < dl:
                tweets.append(data[i])
                i += 1
                
        return tweets
    
with open("trump_tweets_2010~2019.json", "w") as outfile:
    json.dump(save_tweets(), outfile)
    print('ok')