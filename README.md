# WDPII
Projet PPE
Le projet « Wild Dump Prevention II » (WDPII) consiste à prédire l’apparition de déchets sauvages à l’aide d’une intelligence artificielle, selon divers paramètres tels que :
•	Les lieux de dépôts précédemment répertoriés
o	Près d’un cours d’eau

o	Les zones de chantier, de festival et celles fréquentées par des ‘cleanwalkers’

o	Les bords d’autoroute

o	Les discothèques

o	Les espaces verts

•	Des périodes temporelles
o	La saison des tontes

o	Les vacances scolaires

o	Les périodes de déménagements et de fêtes


Afin de discrétiser notre champ d’étude, nous nous sommes focalisés sur 9 arrondissements de Paris de simuler le volume de déchets selon les scénarios dans le cas :
•	D’un quartier dit idéal, exemplaire où le volume de dépôts est peu conséquent
•	D’un espace vert
•	D’un quartier régulièrement sujet aux cleanwalks
•	D’une zone de festival, de chantier et de discothèque
•	D’abords d’autoroute
•	De déménagements
•	De quartier dit insalubre où le volume de dépôts est très important


Dans un premier temps, nous avons implémenté sous Python une carte dont la couleur de la zone varie selon la quantité de déchets (en kg) en fonction du temps. 

![image](https://user-images.githubusercontent.com/120735394/222725378-45e2dbdb-a42a-49bf-9f72-82bea511dbda.png)

Ensuite, nous avons codé notre intelligence artificielle (IA) en Python grâce à l’algorithme LSTM (Long Short Term Memory) afin de prédire les quantités de déchets à venir:

![image](https://user-images.githubusercontent.com/120735394/222725419-875ed08b-916f-4f93-a652-dbaed8f5b755.png)
