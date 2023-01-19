# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium 
from folium import plugins

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