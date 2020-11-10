#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:22:06 2020

@author: yousefnami
"""

import os


artists = []
with os.scandir('/Users/yousefnami/Music/iTunes/iTunes Media/Music') as entries:
    for entry in entries:
        
        artists.append(entry.name)
        
#print(artists) #I have access to the artists

with os.scandir('/Users/yousefnami/Music/iTunes/iTunes Media/Music/2Pac/All Eyez on Me') as entries:
    for entry in entries:
        #print(entry.name)
        pass

import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET #this allows us to parse XML (since the iTunes library file is in XML)

lib_path = '/Users/yousefnami/Music/iTunes/iTunes Music Library.xml'

tree = ET.parse(lib_path)
root = tree.getroot()
main_dict=root.findall('dict')
for item in list(main_dict[0]):    
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))

podcast=[] #All podcast elements
kind = []
purchased=[] # All purchased music
apple_music=[] # Music added to lirary through subscription

column_names = ["Track ID","Total Time","Year","BPM","Date Added","Play Count"\
                ,"Skip Count","Rating","Name","Artist","Genre"]; 
#these are the things we are interested in, manually need to change this

#song_data = dict.fromkeys(column_names,[]) # the dictionary to create our dataframe
song_data = {}
for column in column_names:
    temp_dict = {column : []}
    song_data.update(temp_dict)


for item in tracklist: #item is every song
    x=list(item) # makes a list out of the 'song', which has it's attributes
    temp_columns = []
    for i in range(len(x)): # i is the attribute
        #print(x[i].text)
        if x[i].text in column_names:
            
            #print(x[i].text,x[i+1].text)
            song_data[x[i].text].append(x[i+1].text)
            temp_columns.append(x[i].text)
        missing_data = set(column_names) - set(temp_columns)
    for attribute in missing_data:
        song_data[attribute].append(np.nan)
         
            #print(song_data[x[i].text])
            #print(song_data[x[i].text])
            #print(len(song_data[x[i].text]))
        #if x[i].text == "Name":
         #   name = x[i+1].text
        #if x[i].text == "Kind" and x[i+1].text == "AAC audio file":
          #  print(name)
        
        #print(x[i].text)
        #if x[i].text == "Kind":
          #  print(x[i+1].text)
         #   kind.append(x[i+1].text)
        #if x[i].text == "Kind" and x[i+1].text == "Purchased AAC audio file":
            
        #if x[i].text=="Kind" and x[i+1].text=="MPEG audio file": #
        #    podcast.append(item.getchildren())
#print(song_data)
#print(song_data)
        
        
        
print(song_data)
df = pd.DataFrame(song_data,columns = column_names) #dataframe of the data has been created 
df.to_csv('music_data.csv')dprint(df[['Total Time','Name']]) #note: music length is saved in milliseconds, must convert this !!!!
#print(kind)




