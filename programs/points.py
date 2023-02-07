# -*- coding: utf-8 -*-

import folium
import numpy as np
from folium import plugins
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import pandas as pd
import matplotlib.pyplot as plt
import random
from random import choices
import datetime

m = folium.Map([45.64454, 0.14273],control_scale = True, zoom_start=13)

# heat_data = [[row['latitude'],row['longitude']] for index, row in dataset.iterrows()]
# HeatMap(heat_data, radius = 20, min_opacity = 0.9,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

# lat = float(45.6)
# lon = float(0.10)
# lat_interval = 0.01
# lon_interval = 0.01
# grid = []

# while (lat<=45.7):
#     grid.append([[lat, -180],[lat, 180]])
#     lat = lat + lat_interval

# while (lon<=0.2):
#     grid.append([[-90, lon],[90, lon]])
#     lon = lon + lon_interval
grid = []
grid.append([[45.637087, 0.12 ],[45.667565, 0.12]])
grid.append([[45.637087, 0.15333 ],[45.667565, 0.15333]])
grid.append([[45.637087, 0.18666 ],[45.667565, 0.18666]])
grid.append([[45.637087, 0.22],[45.667565, 0.22]])
grid.append([[45.667565, 0.12],[45.667565, 0.22]])
grid.append([[45.657406, 0.12],[45.657406, 0.22]])
grid.append([[45.647247, 0.12],[45.647247, 0.22]])
grid.append([[45.637087, 0.12],[45.637087, 0.22]])

for g in grid:
    folium.PolyLine(g, color="red", opacity=100).add_to(m)
    
m.save('../maps/maCarte1.html')

#Map des points

#P1  P2  P3  P4
#P5  P6  P7  P8
#P9  P10 P11 P12
#P13 P14 P15 P16

#Dimensions d'un rectangle (exemple: P1-----P2)
#                                    |       | 
#                                    P5-----P6
# Longueur: 2,66666667km
# largeur : 1,25000000km
# Aire    : 3,33333376kmcarré

#Shift Latitude pour chaque point par rapport au point tout au NO: -0.010159
#Shift Longitude par rapport au point tout au NO: +0.173418

#P1:  LAT:45.667565 LON:0.12
#P2:  LAT:45.667565 LON:0.12 
#P3:  LAT:45.667565 LON:0.12 
#P4:  LAT:45.667565 LON:0.12 
#P5:  LAT:45.657406 LON:0.15333
#P6:  LAT:45.657406 LON:0.15333
#P7:  LAT:45.657406 LON:0.15333
#P8:  LAT:45.657406 LON:0.15333
#P9:  LAT:647247 LON:0.18666 
#P10: LAT:647247 LON:0.18666
#P11: LAT:647247 LON:0.18666 
#P12: LAT:647247 LON:0.18666
#P13: LAT:45.637087 LON:0.22
#P14: LAT:45.637087 LON:0.22
#P15: LAT:45.637087 LON:0.22
#P16: LAT:45.637087 LON:0.22