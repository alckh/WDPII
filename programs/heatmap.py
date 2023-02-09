import folium
import numpy as np
from folium import plugins
import matplotlib.pyplot as plt
import folium.plugins
from folium.plugins import HeatMap, HeatMapWithTime
import pandas as pd
import matplotlib.pyplot as plt
import random
from random import choices
import datetime


df= pd.read_excel("BBD_Dechets.xlsm", "Festival", keep_default_na=False, engine='openpyxl')

#heat_data = [[row['latitude'],row['longitude'],row['intensite']] for index, row in df_gps.iterrows()]
index_date = [row['Date'] for index,row in df.iterrows()]
heat_timestamp= [d.strftime('%d/%m/%Y') for d in index_date]

initial_data =  np.random.normal(size=(53, 2)) * np.array([[0.001, 0.001]]) + np.array([[45.65, 0.131]])
move_data = np.random.normal(size=(53, 2)) * 0.0001
data = [(initial_data+i*move_data).tolist() for i in range(53)]

for x in data:
    for row in x:
        weight =100
        row.append(weight)

m = folium.Map([45.64454, 0.14273],control_scale = True, zoom_start=13)

HeatMapWithTime(data, index=heat_timestamp,radius =20, auto_play=True, min_opacity = 0.5,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)
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
