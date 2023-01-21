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
import random

df = pd.read_csv('angouleme_segmenté.csv',encoding='latin-1')

dataset= pd.DataFrame({'latitude':df['latitude'],'longitude':df['longitude'],'intensite':6000})
dataset.to_csv("Dataset_angouleme.csv",index=False, sep=";")
m = folium.Map([45.64454, 0.14273],control_scale = True, zoom_start=13)

heat_data = [[row['latitude'],row['longitude']] for index, row in dataset.iterrows()]
HeatMap(heat_data, radius = 20, min_opacity = 0.9,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')


def Volume_Toxicite(K): #Avec K le nombre de dates pour un même dépôt sauvage
    L_volume=[]
    L_toxicite=[]
    for i in range(0,K):
        v = random.randint(0,3) #Echelle du volume de déchet: 0/Il y a zéro déchet 1/Sac poubelle (ex:30L) 2/Brouette (ex:100L) 3/Camion
        L_volume.append(v)
       
        t = random.randint(1,4) #Echelle de la toxicité: 0/Non toxique pour l'environnement 1/Faiblement toxique 2/Toxique 3/Très toxique 4/Extrêmement toxique
        if v==0: #S'il n'y a pas de déchet la toxicité est de 0
            L_toxicite.append(0)
        else:
            L_toxicite.append(t)
            
    return L_volume, L_toxicite

"""print(Volume_Toxicite(5))"""