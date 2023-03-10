# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:03:16 2023

@author: orlan
"""

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

df = pd.read_excel("../BDD/BDD_EspacesVerts.xlsx")
dataset= pd.DataFrame({'Latitude':df['Latitude'],'Longitude':df['Longitude'],'intensite':6000})
m = folium.Map([45.64454, 0.14273],control_scale = True, zoom_start=13)
heat_data = [[row['Latitude'],row['Longitude']] for index, row in dataset.iterrows()]
HeatMap(heat_data, radius = 20, min_opacity = 0.9,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

df_constante = pd.read_excel("../BDD/BDD_Constante.xlsx")
dataset2= pd.DataFrame({'Latitude':df_constante['Latitude'],'Longitude':df_constante['Longitude'],'intensite':6000})
heat_data2 = [[row['Latitude'],row['Longitude']] for index, row in dataset2.iterrows()]
HeatMap(heat_data2, radius = 20, min_opacity = 0.9,gradient={.6: 'yellow', .98: 'orange', 1: 'red'}).add_to(m)

df_disco = pd.read_excel("../BDD/BDD_Discotheque.xlsx")
dataset3= pd.DataFrame({'Latitude':df_disco['Latitude'],'Longitude':df_disco['Longitude'],'intensite':6000})
heat_data3 = [[row['Latitude'],row['Longitude']] for index, row in dataset3.iterrows()]
HeatMap(heat_data3, radius = 20, min_opacity = 0.9,gradient={1: 'yellow', 1: 'orange',1:'red'}).add_to(m)

df_chantier = pd.read_excel("../BDD/BDD_Chantier.xlsx")
dataset4= pd.DataFrame({'Latitude':df_chantier['Latitude'],'Longitude':df_chantier['Longitude'],'intensite':6000})
heat_data4 = [[row['Latitude'],row['Longitude']] for index, row in dataset3.iterrows()]
HeatMap(heat_data4, radius = 20, min_opacity = 0.9,gradient={1: 'yellow', 1: 'orange',1:'red'}).add_to(m)




grid = []
grid.append([[45.637087, 0.12 ],[45.667565, 0.12]])
grid.append([[45.637087, 0.15333 ],[45.667565, 0.15333]])
grid.append([[45.637087, 0.18666 ],[45.667565, 0.18666]])
grid.append([[45.637087, 0.22],[45.667565, 0.22]])
grid.append([[45.667565, 0.12],[45.667565, 0.22]])
grid.append([[45.657406, 0.12],[45.657406, 0.22]])
grid.append([[45.647247, 0.12],[45.647247, 0.22]])
grid.append([[45.637087, 0.12],[45.637087, 0.22]])


folium.Marker([45.662898, 0.135],popup= 'Zone festival' ).add_to(m)
folium.Marker([45.662898, 0.17],popup='Quartier r??fuli??rement sujet aux cleanwalk').add_to(m)
folium.Marker([45.662898, 0.20],popup='Quartier insalubre').add_to(m)
folium.Marker([45.651889, 0.135],popup='D??m??nagements').add_to(m)
folium.Marker([45.651889, 0.17],popup='Quartier id??al').add_to(m)
folium.Marker([45.651889, 0.20],popup='Espaces verts').add_to(m)
folium.Marker([45.640000, 0.135],popup='Abords autoroute').add_to(m)
folium.Marker([45.640000, 0.17],popup='Zone en chantier').add_to(m)
folium.Marker([45.640000, 0.20],popup='Zone avec discoth??ques').add_to(m)


for g in grid:
    folium.PolyLine(g, color="red", opacity=100).add_to(m)
    
m.save('../maps/maCarte1.html')



#CAfficher les courbes de nocivit?? et de volume en fonction des diff??rents sc??anarii
def graph_excel(nom_classeur):
    df = pd.read_excel(nom_classeur) 

    date = df['Date'].tolist()
    volume = df['Volume'].tolist()
    nocivite = df['Nocivit??'].tolist()

    plt.title("Evolution " + nom_classeur)
    plt.plot(date,volume, label='Volume')
    plt.plot(date,nocivite, label='Nocivit??')
    plt.xlabel('Temps')
    plt.xticks(rotation=90)
    plt.ylabel('Valeur')
    plt.legend()
    plt.show()

graph_excel("../BDD/BDD_Chantier.xlsx")
graph_excel("../BDD/BDD_Demenagement.xlsx")
graph_excel("../BDD/BDD_EspacesVerts.xlsx")
graph_excel("../BDD/BDD_Festival.xlsx")
graph_excel("../BDD/BDD_GroupeScolaire.xlsx")
graph_excel("../BDD/BDD_QuartierCatastrophe.xlsx")
graph_excel("../BDD/BDD_QuartierExemplaire.xlsx")
graph_excel("../BDD/BDD_ScolaireEspacesVerts.xlsx")














"""start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2022, 1, 1)
nb_date = 5
col_date = [i for i in range(1,nb_date+1)]
df_data_date= dataset.set_index(['latitude','longitude'])
column_date=[]
for x in range(1,nb_date+1):
    numeroter = "Date" + str(x)
    column_date.append(numeroter)
df_data_date= df_data_date.reindex(columns= column_date)
df_data_date.to_csv("Dataset_angouleme.csv", sep=";")

print(df_data_date)

def random_date(start,end, nb_date):
    rand_date = []
    while start<=end:
        rand_date.append(start)
        start += datetime.timedelta(days=1)
    rand_date= choices(rand_date,k=nb_date)
    return sorted(rand_date)

df_data_date.iloc[:]= random_date(start_date,end_date,nb_date)
index_date= df_data_date.to_numpy()



def Volume_Toxicite(K):  # Avec K le nombre de dates pour un m??me d??p??t sauvage
    L_volume = []
    L_toxicite = []
    for i in range(0, K):
        v = random.randint(0,3)  # Echelle du volume de d??chet: 0/Il y a z??ro d??chet 1/Sac poubelle (ex:30L) 2/Brouette (ex:100L) 3/Camion
        L_volume.append(v)

        t = random.randint(1,4)  # Echelle de la toxicit??: 0/Non toxique pour l'environnement 1/Faiblement toxique 2/Toxique 3/Tr??s toxique 4/Extr??mement toxique
        if v == 0:  # S'il n'y a pas de d??chet la toxicit?? est de 0
            L_toxicite.append(0)
        else:
            L_toxicite.append(t)

    return L_volume, L_toxicite


#print(Volume_Toxicite(5))
plt.title("Evolution du volume de d??chet ?? un lieu donn??")
plt.plot(index_date[0],Volume_Toxicite(nb_date)[0])
plt.xlabel('Temps')
plt.xticks(rotation=90)
plt.ylabel('Volume')
plt.show()
"""