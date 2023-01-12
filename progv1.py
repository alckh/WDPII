# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium 
from folium import plugins

data =[[    40.7726,    -73.9568,   1900.    ],
       [    40.7785,    -73.9556,   3200.    ],
       [    40.7216,    -73.9809,   5800.    ],
       [    40.7384,    -73.9848,   2900.    ],
       [    40.7678,    -73.9915,   3312.    ],
       [    40.7659,    -73.9574,   2600.    ],
       [    40.7092,    -74.0137,   4299.    ],
       [    40.7384,    -73.982 ,   5750.    ],
       [    40.7312,    -73.9896,   3595.    ]]

m = folium.Map([40.7726,    -73.9568], 
               control_scale = True, zoom_start=11)

plugins.HeatMap(data, radius = 20, min_opacity = 0.1, max_val = 50,gradient={.6: 'blue', .98: 'lime', 1: 'red'}).add_to(m)
m.save('maCarte1.html')