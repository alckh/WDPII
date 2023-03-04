# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:18:52 2023

@author: celia
"""
import pandas as pd
import geopandas as gpd
import plotly.express as px

#Recuperation des data
df = pd.read_csv("../BDD/BDD_Paris30.csv")
geo_df = gpd.read_file('../data/arrondissements.geojson', driver='GeoJSON')
df = df[['id', 'scenario', 'volume_continu_ia','date']]

#Formatage des dates
df=df.sort_values(by=['date'])
df['date']=pd.to_datetime(df['date'], errors='coerce')
df['date']= df['date'].dt.strftime('%Y-%m-%d')

#Merging entre localisation et scenario
geo_df = geo_df[['scenario', 'geometry']]
geo_count_df = pd.merge(geo_df, df, on='scenario')
geo_count_df=geo_count_df.sort_values(by=['date']) #tri par dates

#Reset id pour les divers scénarios
geo_count_df.loc[geo_count_df['scenario']=='Quartier insalubre', 'id']=0
geo_count_df.loc[geo_count_df['scenario']=='Quartier regulierement sujet aux cleanwalk', 'id']=1
geo_count_df.loc[geo_count_df['scenario']=='Abords autoroute', 'id']=2
geo_count_df.loc[geo_count_df['scenario']=='Espaces verts', 'id']=3
geo_count_df.loc[geo_count_df['scenario']=='Quartier ideal', 'id']=4
geo_count_df.loc[geo_count_df['scenario']=='Zone avec discotheque', 'id']=5
geo_count_df.loc[geo_count_df['scenario']=='Demenagements', 'id']=6
geo_count_df.loc[geo_count_df['scenario']=='Zone festival', 'id']=7
geo_count_df.loc[geo_count_df['scenario']=='Zone en chantier', 'id']=8

#Creation d'une carte avec un timeslider
fig=px.choropleth_mapbox(data_frame=geo_count_df,
                         geojson=geo_df,
                         locations=geo_count_df['id'],
                         color=geo_count_df['volume_continu_ia'].astype(float),
                         labels={'color':'Quantité de déchets en kg'},
                         opacity=0.6,
                         center={'lat':48.866804569664794, 'lon':2.336997985839844},
                         mapbox_style='open-street-map',
                         hover_name='scenario',
                         zoom=10,
                         color_continuous_scale='ylorrd',
                         range_color=(0,max(df['volume_continu_ia'])),
                         animation_frame='date',
                         width=800,
                         height=600,
                         title="Prédiction du volume de déchets sauvages au cours du temps")
fig.write_html('../maps/mapping_IA.htlm')
fig.show()
