# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium
import numpy as np
from folium import plugins
import pandas as pd
import requests
import json

x = '[{"latitude":43.41800914565575,"longitude":-1.4736806863206051,"town":"Ustaritz","postcode":"64480","epci":"CA du Pays Basque","county":"Pyrénées-Atlantiques","images":["https://api.v2.clean2gether.com/uploads/c2g_upload_ee31b829ca.jpg"]},{"latitude":43.42567782128301,"longitude":-1.4851003904940752,"town":"Arcangues","postcode":"64200","epci":"CA du Pays Basque","county":"Pyrénées-Atlantiques","images":["https://api.v2.clean2gether.com/uploads/c2g_upload_4a96cf89ac.jpg"]}]'

y = json.loads(x)
data = np.zeros((len(y),4))

for i in range(len(y)):
       data[i][0]=y[i]["latitude"]
       data[i][1]=y[i]["longitude"]
       data[i][2] = 6000
       data[i][3] = 20

m = folium.Map([45.6754, 0.24273],
               control_scale = True, zoom_start=11)

plugins.HeatMap(data, radius = 20, min_opacity = 0.1, max_val = 50,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')
