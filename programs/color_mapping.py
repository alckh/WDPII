import pandas as pd
import geopandas as gpd
import plotly.express as px

#Recuperation des data
listing_df = pd.read_csv("../BDD/BDD_Paris_CSV2.csv")
nbh_geo_df = gpd.read_file('arrondissementscopie.geojson', driver='GeoJSON')
listing_df = listing_df[['id', 'scenario', 'volumecontinu','date']]

#Formatage des dates
listing_df=listing_df.sort_values(by=['date'])
listing_df['date']=pd.to_datetime(listing_df['date'], errors='coerce')
listing_df['date']= listing_df['date'].dt.strftime('%Y-%m-%d')

#Merging entre localisation et scenario
nbh_geo_df = nbh_geo_df[['scenario', 'geometry']]
nbh_geo_count_df = pd.merge(nbh_geo_df, listing_df, on='scenario')
nbh_geo_count_df=nbh_geo_count_df.sort_values(by=['date']) #tri par dates

#Reset id pour les divers scénarios
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Quartier insalubre', 'id']=0
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Quartier regulierement sujet aux cleanwalk', 'id']=1
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Abords autoroute', 'id']=2
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Espaces verts', 'id']=3
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Quartier ideal', 'id']=4
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Zone avec discotheque', 'id']=5
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Demenagements', 'id']=6
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Zone festival', 'id']=7
nbh_geo_count_df.loc[nbh_geo_count_df['scenario']=='Zone en chantier', 'id']=8

#Creation d'une carte avec un timeslider
fig=px.choropleth_mapbox(data_frame=nbh_geo_count_df,
                         geojson=nbh_geo_df,
                         locations=nbh_geo_count_df['id'],
                         color=nbh_geo_count_df['volumecontinu'].astype(float),
                         labels={'color':'Quantité de déchets en kg'},
                         opacity=0.6,
                         center={'lat':48.866804569664794, 'lon':2.336997985839844},
                         mapbox_style='open-street-map',
                         hover_name='scenario',
                         zoom=10,
                         color_continuous_scale='ylorrd',
                         range_color=(0,max(listing_df['volumecontinu'])),
                         animation_frame='date',
                         width=800,
                         height=600,
                         title='Evolution du volume de déchets sauvages au cours du temps')
fig.write_html('mapping.htlm')
fig.show()
