# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

import folium 
from folium import plugins

data =[[    48.8514,    2.2886,   1900.    ],
       [    48.8514,    2.2886,   3200.    ],
       [    48.8514,    2.2886,   5800.    ],
       [    48.8514,    2.2886,   2900.    ],
       [    48.8514,    2.2886,   3312.    ],
       [    48.8514,    2.2886,   2600.    ],
       [    48.8514,    2.2886,   4299.    ],
       [    48.8514,    2.2886,   5750.    ],
       [    48.8514,    2.2886,   3595.    ]]

m = folium.Map([48.8514, 2.2887],
               control_scale = True, zoom_start=11)

plugins.HeatMap(data, radius = 20, min_opacity = 0.1, max_val = 50,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

m.save('maCarte1.html')