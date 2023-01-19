# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium 
from folium import plugins

import json


x = '[{"latitude":43.41800914565575,"longitude":-1.4736806863206051,"town":"Ustaritz","postcode":"64480","epci":"CA du Pays Basque","county":"Pyrénées-Atlantiques","images":["https://api.v2.clean2gether.com/uploads/c2g_upload_ee31b829ca.jpg"]},{"latitude":43.42567782128301,"longitude":-1.4851003904940752,"town":"Arcangues","postcode":"64200","epci":"CA du Pays Basque","county":"Pyrénées-Atlantiques","images":["https://api.v2.clean2gether.com/uploads/c2g_upload_4a96cf89ac.jpg"]}]'

y = json.loads(x)

print(y[0]["latitude"])
print(y[1]["latitude"])



data =[[    45.6754,    0.24273,   6000.    ],
       [    45.59092,    0.27279,   5200.    ],
       [    45.54825,    0.12207,   5800.    ],
       [    45.64459,    0.11869,   5900.    ],
       [    45.70302,    -0.30443,  5312.    ],
       [    45.63751,    0.14252,   5600.    ]]

m = folium.Map([45.6754, 0.24273],
               control_scale = True, zoom_start=11)

plugins.HeatMap(data, radius = 20, min_opacity = 0.1, max_val = 50,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')