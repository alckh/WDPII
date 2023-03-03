# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:35:35 2023

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM
import math
from sklearn.preprocessing import MinMaxScaler


#lecture des donnees sur excel
df = []
df.append(pd.read_excel("../BDD/BDD_Chantier.xlsx"))
"""
df.append(pd.read_excel("../BDD/BDD_Demenagement.xlsx"))
df.append(pd.read_excel("../BDD/BDD_Discotheque.xlsx"))
df.append(pd.read_excel("../BDD/BDD_EspacesVerts.xlsx"))
df.append(pd.read_excel("../BDD/BDD_Festival.xlsx"))
df.append(pd.read_excel("../BDD/BDD_QuartierAise.xlsx"))
df.append(pd.read_excel("../BDD/BDD_QuartierMalFrequente.xlsx"))
df.append(pd.read_excel("../BDD/BDD_ScenarioPositif.xlsx"))
df.append(pd.read_excel("../BDD/BDD_Constante.xlsx"))
"""

#test de l'IA sur les 9 scenarios (pour ajouter un fichier il faut continuer la liste)
for j in range (0,len(df)):
        

        volume_data = df[j].filter(['Volume continu'])          # Creer une colonne nommee volume continu
        
        dataset= volume_data.values                             # Tableau 2D des valeurs du dataset
        
        scaler = MinMaxScaler(feature_range=(0, 1))             # Normaliser les valeurs du dataset
        scaled_data = scaler.fit_transform(dataset)             # vient de sklearn.preprocessing. fit calcule la moyenne et la variance de chaque variables. transform transforme les variables en utilisant la moyenne et la variance trouvee. xscaled= (x - mean)/standarddeviation
        
        training_data_len = math.ceil(len(dataset) *.7)         # Prendre 70% des datas
        train_data = scaled_data[0:training_data_len  , : ]     # train_data reçoit les 70% de data precedemment extraites
        
        # separation des donnees
        x_train_data=[] 
        y_train_data =[]
        
        for i in range(30,len(train_data)):
            # Cast des array en list pour pouvoir ajouter des elements differents
            x_train_data=list(x_train_data)                     
            y_train_data=list(y_train_data)
            # Slice les donnees de i-29 a i -> on prend 30 valeurs pour x 
            x_train_data.append(train_data[i-30:i,0])
            # On prend les 30 valeurs pour y
            y_train_data.append(train_data[i,0])
         
            # Conversion list vers array
            x_train_data1, y_train_data1 = np.array(x_train_data), np.array(y_train_data)
         
            # Convesion de x_train_data1 en array d'array a x_train_data1.shape[0] lignes et x_train_data1.shape[1] colonnes
            x_train_data2 = np.reshape(x_train_data1, (x_train_data1.shape[0],x_train_data1.shape[1],1))
        
            
        model = Sequential()                                                                            # Model keras Neural network sequential model
        model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train_data2.shape[1],1)))         # model LSTM avec output de tout les hidden state h (output de chaque cellule d'un layer)
        model.add(LSTM(units=50, return_sequences=False))                                               # on empile deux modeles LSTM, d'où le return_sequences=True pour le 1er) "You must set return_sequences=True when stacking LSTM layers so that the second LSTM layer has a three-dimensional sequence input."
        model.add(Dense(units=25))                                                                      # Une couche de hidden layer avec 25 neurones.
        model.add(Dense(units=1))                                                                       # Une couche de hidden layer avec 1 neurone
        
        model.compile(optimizer='adam', loss='mean_squared_error')                                      # L'optimisation d'Adam est une methode de descente de gradient stochastique qui repose sur l'estimation adaptative des moments d'ordre 1 et 2. MSE calcule la moyenne des carres des erreurs entre les labels et les predictions.
        model.fit(x_train_data2, y_train_data1, batch_size=1, epochs=400)                               # mettre les datas dans le modele afin de pouvoir commencer la prediction. La taille du batch est un nombre d'echantillons traites avant que le modele ne soit mis a jour. Le nombre d'epochs est le nombre de passages complets dans l'ensemble de donnees d'apprentissage.

        
        # Test data
        test_data = scaled_data[training_data_len - 30: , : ]
        x_test = []
        y_test =  dataset[training_data_len : , : ]
        for i in range(30,len(test_data)): # similaire au training
            x_test.append(test_data[i-30:i,0]) # similaire au training
         
        # Convertir les list en array parce que model.predict ne prend en parametre que des numpy array
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))
         
        # Prediction a partir de la data de test
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)     # Obtenir la data original (non normalisee)
        
        rmse=np.sqrt(np.mean(((predictions- y_test)**2)))       # Mean squared error
        print(rmse)
        
        train = df[j][:training_data_len]                       # dataframe (tableau 2D) comprenant toutes les valeurs pour le plot
        valid = df[j][training_data_len:]                       # dataframe (tableau 2D) comprenant toutes les valeurs pour le plot
         
        valid['Predictions'] = predictions
         
        plt.title('Model')
        plt.xlabel('Date')
        plt.ylabel('Volume')
         
        plt.plot(train['Volume continu'])
        plt.plot(valid[['Volume continu', 'Predictions']])
         
        plt.legend(['Train', 'Test', 'Predictions'], loc='lower left')
         
        plt.show()

#Batch size: Total number of training examples present in a single batch.
#Epochs: One Epoch is when an ENTIRE dataset is passed forward and backward through the neural network only ONCE.