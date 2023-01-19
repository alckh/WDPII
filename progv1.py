# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium
import numpy as np
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_csv('angouleme.csv',encoding='latin-1')
df.drop(df[(df['town']!="AngoulÇ¦me")].index, inplace=True)
df.reset_index(inplace = True, drop = True)

dataset= pd.DataFrame({'latitude':df['latitude'],'longitude':df['longitude'],'intensite':6000})

m = folium.Map([45.6754, 0.24273],control_scale = True, zoom_start=11)

heat_data = [[row['latitude'],row['longitude']] for index, row in dataset.iterrows()]
HeatMap(heat_data, radius = 20, min_opacity = 0.1,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')
