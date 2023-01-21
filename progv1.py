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

df = pd.read_csv('angouleme_segmenté.csv',encoding='latin-1')

dataset= pd.DataFrame({'latitude':df['latitude'],'longitude':df['longitude'],'intensite':6000})
dataset.to_csv("Dataset_angouleme.csv",index=False, sep=";")
m = folium.Map([45.64454, 0.14273],control_scale = True, zoom_start=13)

heat_data = [[row['latitude'],row['longitude']] for index, row in dataset.iterrows()]
HeatMap(heat_data, radius = 20, min_opacity = 0.9,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')

