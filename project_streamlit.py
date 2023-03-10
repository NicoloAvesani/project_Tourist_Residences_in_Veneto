import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression


tourism_structures_df = pd.read_csv('https://www.veneto.eu/static/opendata/dove-alloggiare.csv')

code_original_info = '''
RangeIndex: 8504 entries, 0 to 8503
Data columns (total 45 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   PROVINCIA              8504 non-null   object 
 1   COMUNE                 8504 non-null   object 
 2   LOCALITA               1573 non-null   object 
 3   TIPOLOGIA              8504 non-null   object 
 4   TIPOLOGIA SECONDARIA   3695 non-null   object 
 5   DENOMINAZIONE          8504 non-null   object 
 6   INDIRIZZO              8486 non-null   object 
 7   NUMERO CIVICO          8162 non-null   object 
 8   INTERNO                289 non-null    object 
 9   CAP                    8471 non-null   float64
 10  TELEFONO               8415 non-null   object 
 11  FAX                    5010 non-null   object 
 12  EMAIL                  8473 non-null   object 
 13  SITO WEB               5725 non-null   object 
 14  ZONA                   8504 non-null   object 
 15  PISCINA                8504 non-null   object 
 16  PISCINA COPERTA        8504 non-null   object 
 17  RISTORANTE             8504 non-null   object 
 18  PARCHEGGIO             8504 non-null   object 
 19  SALA CONFERENZE        8504 non-null   object 
 20  ARIA CONDIZIONATA      8504 non-null   object 
 21  GIOCHI BIMBI           8504 non-null   object 
 22  SAUNA                  8504 non-null   object 
 23  SOLARIUM               8504 non-null   object 
 24  FITNESS                8504 non-null   object 
 25  ANIMALI AMMESSI        8504 non-null   object 
 26  CENTRO STORICO         8504 non-null   object 
 27  ZONA FIERA             8504 non-null   object 
 28  LAGO                   8504 non-null   object 
 29  AEROPORTO              8504 non-null   object 
 30  AUTOSTRADA             8504 non-null   object 
 31  IMPIANTI RISALITA      8504 non-null   object 
 32  STAZIONE FS            8504 non-null   object 
 33  MARE                   8504 non-null   object 
 34  TERMALE                8504 non-null   object 
 35  PERIFERIA              8504 non-null   object 
 36  COLLINARE              8504 non-null   object 
 37  INGLESE                8504 non-null   object 
 38  FRANCESE               8504 non-null   object 
 39  TEDESCO                8504 non-null   object 
 40  SPAGNOLO               8504 non-null   object 
 41  CHIUSURA TEMPORANEA    8504 non-null   object 
 42  CODICE IDENTIFICATIVO  8504 non-null   int64  
 43  DATA ULTIMA MODIFICA   8504 non-null   object 
 44  CLASSIFICAZIONE        7337 non-null   object 
dtypes: float64(1), int64(1), object(43)'''

code_map='''
for i in range(len(tourism_structures_df)):
  for j in tourism_structures_df.columns:
    if (tourism_structures_df[j][i] == 'Vero') | (tourism_structures_df[j][i] == 'Falso'):
      tourism_structures_df[j] = tourism_structures_df[j].map({'Vero':1,'Falso':0}) 
'''

## Since the majority of data are string values, so I need to transform them into boolean values with 1 for True(Vero) and 0 for False (Falso)

for i in range(len(tourism_structures_df)):
  for j in tourism_structures_df.columns:
    if (tourism_structures_df[j][i] == 'Vero') | (tourism_structures_df[j][i] == 'Falso'):
      tourism_structures_df[j] = tourism_structures_df[j].map({'Vero':1,'Falso':0}) 


## i want to see the informations of the adjusted dataset

tourism_structures_df.info()

## as i can see, the dataset has a total of 8504 entries and 45 clolumns

code_adj_info = '''
RangeIndex: 8504 entries, 0 to 8503
Data columns (total 45 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   PROVINCIA              8504 non-null   object 
 1   COMUNE                 8504 non-null   object 
 2   LOCALITA               1573 non-null   object 
 3   TIPOLOGIA              8504 non-null   object 
 4   TIPOLOGIA SECONDARIA   3695 non-null   object 
 5   DENOMINAZIONE          8504 non-null   object 
 6   INDIRIZZO              8486 non-null   object 
 7   NUMERO CIVICO          8162 non-null   object 
 8   INTERNO                289 non-null    object 
 9   CAP                    8471 non-null   float64
 10  TELEFONO               8415 non-null   object 
 11  FAX                    5010 non-null   object 
 12  EMAIL                  8473 non-null   object 
 13  SITO WEB               5725 non-null   object 
 14  ZONA                   8504 non-null   object 
 15  PISCINA                8504 non-null   int64  
 16  PISCINA COPERTA        8504 non-null   int64  
 17  RISTORANTE             8504 non-null   int64  
 18  PARCHEGGIO             8504 non-null   int64  
 19  SALA CONFERENZE        8504 non-null   int64  
 20  ARIA CONDIZIONATA      8504 non-null   int64  
 21  GIOCHI BIMBI           8504 non-null   int64  
 22  SAUNA                  8504 non-null   int64  
 23  SOLARIUM               8504 non-null   int64  
 24  FITNESS                8504 non-null   int64  
 25  ANIMALI AMMESSI        8504 non-null   int64  
 26  CENTRO STORICO         8504 non-null   int64  
 27  ZONA FIERA             8504 non-null   int64  
 28  LAGO                   8504 non-null   int64  
 29  AEROPORTO              8504 non-null   int64  
 30  AUTOSTRADA             8504 non-null   int64  
 31  IMPIANTI RISALITA      8504 non-null   int64  
 32  STAZIONE FS            8504 non-null   int64  
 33  MARE                   8504 non-null   int64  
 34  TERMALE                8504 non-null   int64  
 35  PERIFERIA              8504 non-null   int64  
 36  COLLINARE              8504 non-null   int64  
 37  INGLESE                8504 non-null   int64  
 38  FRANCESE               8504 non-null   int64  
 39  TEDESCO                8504 non-null   int64  
 40  SPAGNOLO               8504 non-null   int64  
 41  CHIUSURA TEMPORANEA    8504 non-null   int64  
 42  CODICE IDENTIFICATIVO  8504 non-null   int64  
 43  DATA ULTIMA MODIFICA   8504 non-null   object 
 44  CLASSIFICAZIONE        7337 non-null   object '''

ts_desriptive_mean = tourism_structures_df.describe().T['mean']

tr_groupby_mean = tourism_structures_df.groupby(['PROVINCIA']).mean()

## create a copy of the original dataframe in order to drop some problematic and useless columns that I will not use in my analysis.
## 'Problematic' since they have null values.

## The dropped columns are: LOCATION, SECONDARY TYPE, ADDRESS, HOUSE NUMBER, INTERNAL, ZIP CODE, PHONE, FAX, EMAIL ADDRESS, WEBSITE, AREA, LAST EDIT, IDENTIFICATION CODE.
## These columns provide useless information, since they concern only the single residential facility, and are linked to contact information. 
## The columns I am interested in are those which provide me information about the presence or not of descriptive characteristics of the tourist residences

## I also drop the following columns that, even if they provide information about descriptive characteristics, are not relevant for my purposes:
## INDOOR SWIMMING POOL, CONFERENCE ROOM, SOLARIUM, OUTSKIRTS, HILLS

tourism_df = tourism_structures_df.copy()

tourism_df = tourism_df.drop(tourism_df.columns[[2,4,6,7,8,9,10,11,12,13,14,16,19,23,35,36,42,43]],axis=1)


code_cleaned_df = '''
RangeIndex: 8504 entries, 0 to 8503
Data columns (total 27 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   PROVINCIA             8504 non-null   object
 1   COMUNE                8504 non-null   object
 2   TIPOLOGIA             8504 non-null   object
 3   DENOMINAZIONE         8504 non-null   object
 4   PISCINA               8504 non-null   int64 
 5   RISTORANTE            8504 non-null   int64 
 6   PARCHEGGIO            8504 non-null   int64 
 7   ARIA CONDIZIONATA     8504 non-null   int64 
 8   GIOCHI BIMBI          8504 non-null   int64 
 9   SAUNA                 8504 non-null   int64 
 10  FITNESS               8504 non-null   int64 
 11  ANIMALI AMMESSI       8504 non-null   int64 
 12  CENTRO STORICO        8504 non-null   int64 
 13  ZONA FIERA            8504 non-null   int64 
 14  LAGO                  8504 non-null   int64 
 15  AEROPORTO             8504 non-null   int64 
 16  AUTOSTRADA            8504 non-null   int64 
 17  IMPIANTI RISALITA     8504 non-null   int64 
 18  STAZIONE FS           8504 non-null   int64 
 19  MARE                  8504 non-null   int64 
 20  TERMALE               8504 non-null   int64 
 21  INGLESE               8504 non-null   int64 
 22  FRANCESE              8504 non-null   int64 
 23  TEDESCO               8504 non-null   int64 
 24  SPAGNOLO              8504 non-null   int64 
 25  CHIUSURA TEMPORANEA   8504 non-null   int64 
 26  CLASSIFICAZIONE       7337 non-null   object
dtypes: int64(22), object(5)'''

## firstly, I must drop the null values rows and change the indexes

classification_nan_mask = tourism_df['CLASSIFICAZIONE'].isnull()
tourism_clear_class_df = tourism_df[classification_nan_mask == False]

new_indexes = []
for i in range(len(tourism_clear_class_df)):
    new_indexes.append(i)

tourism_clear_class_df.index = new_indexes

code_class_unique = '''array(['1 *', '2 **', '2 Leoni', '3 ***', '3 *** SUPERIOR', '3 Leoni',
       '4 ****', '4 **** SUPERIOR', '4 Leoni', '5 *****', '5 ***** lusso',
       '5 Leoni'], dtype=object)'''

## I create new columns relative to different class of tourist residences


class_1 = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '1 *':
    class_1.append(1)
  else:
    class_1.append(0)

tourism_clear_class_df['CLASS 1'] = class_1


class_2 = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '2 **':
    class_2.append(1)
  else:
    class_2.append(0)

tourism_clear_class_df['CLASS 2'] = class_2

class_2_Leoni = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '2 Leoni':
    class_2_Leoni.append(1)
  else:
    class_2_Leoni.append(0)

tourism_clear_class_df['CLASS 2 Leoni'] = class_2_Leoni

class_3 = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '3 ***' :
    class_3.append(1)
  else:
    class_3.append(0)

tourism_clear_class_df['CLASS 3'] = class_3

class_3_Leoni = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '3 Leoni' :
    class_3_Leoni.append(1)
  else:
    class_3_Leoni.append(0)

tourism_clear_class_df['CLASS 3 Leoni'] = class_3_Leoni

class_3_sup = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '3 *** SUPERIOR' :
    class_3_sup.append(1)
  else:
    class_3_sup.append(0)

tourism_clear_class_df['CLASS 3 SUPERIOR'] = class_3_sup

class_4 = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '4 ****':
    class_4.append(1)
  else:
    class_4.append(0)

tourism_clear_class_df['CLASS 4'] = class_4

class_4_Leoni = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '4 Leoni' :
    class_4_Leoni.append(1)
  else:
    class_4_Leoni.append(0)

tourism_clear_class_df['CLASS 4 Leoni'] = class_4_Leoni

class_4_sup = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '4 **** SUPERIOR' :
    class_4_sup.append(1)
  else:
    class_4_sup.append(0)

tourism_clear_class_df['CLASS 4 SUPERIOR'] = class_4_sup

class_5 = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '5 *****':
    class_5.append(1)
  else:
    class_5.append(0)

tourism_clear_class_df['CLASS 5'] = class_5

class_5_Leoni = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '5 Leoni':
    class_5_Leoni.append(1)
  else:
    class_5_Leoni.append(0)

tourism_clear_class_df['CLASS 5 Leoni'] = class_5_Leoni

class_5_luxury = []

for i in range(len(tourism_clear_class_df)):
  if tourism_clear_class_df['CLASSIFICAZIONE'][i] == '5 ***** lusso':
    class_5_luxury.append(1)
  else:
    class_5_luxury.append(0)

tourism_clear_class_df['CLASS 5 LUXURY'] = class_5_luxury


## I also create an all lenguages column in which I will have 1 if the tourist residence speak all 4 lenguages

languages = []

for i in range(len(tourism_clear_class_df)):
    if (tourism_clear_class_df.loc[i, 'INGLESE'] == 1) & (tourism_clear_class_df.loc[i, 'TEDESCO'] == 1) & (tourism_clear_class_df.loc[i, 'FRANCESE'] == 1) & (tourism_clear_class_df.loc[i, 'SPAGNOLO'] == 1):
        languages.append(1)
    else:
        languages.append(0)

tourism_clear_class_df['LANGUAGES'] = languages


tourism_clear_class_groupby_mean = tourism_clear_class_df.groupby(['PROVINCIA']).mean()



## Now I can understand how many tourist residences by provincia has the characteristics in index

tourism_clear_class_groupby_sum = tourism_clear_class_df.groupby(['PROVINCIA']).sum()



## I create masks and df for every provincia

belluno_mask = tourism_clear_class_df['PROVINCIA'] == 'BELLUNO'
belluno_df = tourism_clear_class_df[belluno_mask]

padova_mask = tourism_clear_class_df['PROVINCIA'] == 'PADOVA'
padova_df = tourism_clear_class_df[padova_mask]

rovigo_mask = tourism_clear_class_df['PROVINCIA'] == 'ROVIGO'
rovigo_df = tourism_clear_class_df[rovigo_mask]

treviso_mask = tourism_clear_class_df['PROVINCIA'] == 'TREVISO'
treviso_df = tourism_clear_class_df[treviso_mask]

venezia_mask = tourism_clear_class_df['PROVINCIA'] == 'VENEZIA'
venezia_df = tourism_clear_class_df[venezia_mask]

verona_mask = tourism_clear_class_df['PROVINCIA'] == 'VERONA'
verona_df = tourism_clear_class_df[verona_mask]

vicenza_mask = tourism_clear_class_df['PROVINCIA'] == 'VICENZA'
vicenza_df = tourism_clear_class_df[vicenza_mask]

## length of the dfs that I have just created gives me the number of tourist residences by provincia

belluno_tr = len(belluno_df)

padova_tr = len(padova_df)

treviso_tr = len(treviso_df)

rovigo_tr = len(rovigo_df)

venezia_tr = len(venezia_df)

verona_tr = len(verona_df)

vicenza_tr = len(vicenza_df)

city_len = [belluno_tr , padova_tr, treviso_tr, rovigo_tr, venezia_tr, verona_tr, vicenza_tr]

belluno_descriptive = tourism_clear_class_groupby_sum.T['BELLUNO']
padova_descriptive = tourism_clear_class_groupby_sum.T['PADOVA']
treviso_descriptive = tourism_clear_class_groupby_sum.T['TREVISO']
rovigo_descriptive = tourism_clear_class_groupby_sum.T['ROVIGO']
venezia_descriptive = tourism_clear_class_groupby_sum.T['VENEZIA']
verona_descriptive = tourism_clear_class_groupby_sum.T['VERONA']
vicenza_descriptive = tourism_clear_class_groupby_sum.T['VICENZA']

city_list = [belluno_descriptive, padova_descriptive, treviso_descriptive, rovigo_descriptive, venezia_descriptive, verona_descriptive, vicenza_descriptive]

st.title('Tourist Residences in Veneto :lion_face:')
st.subheader('Nicol?? Avesani VR490189, Final Project')
st.sidebar.write("What do you want to see?")

if st.sidebar.checkbox("INFO AND LEGEND"):

  st.write('Welcome! My name is Nicol?? Avesani, and this is my project. I have choosen a dataset called **Tourist Residences in Veneto**, which describes the main descriptive variables of accommodation facilities in Veneto.')
  

  city_coordinates = {
    'Belluno': [46.13, 12.21],
    'Padova': [45.40, 11.87],
    'Rovigo': [45.067, 11.795],
    'Treviso': [45.66, 12.24],
    'Venezia': [45.44, 12.33],
    'Verona': [45.44, 10.99],
    'Vicenza': [45.55, 11.54]
  }

  marker_data = [(name, lat, lon) for name, (lat, lon) in city_coordinates.items()]

  df = pd.DataFrame(marker_data, columns=['name', 'lat', 'lon'])

  st.write("""# Map of Provinces in Veneto""")
  st.write('This is the map with the 7 **Province**. There are 7 Districts in Veneto (Belluno, Padova, Rovigo, Treviso, Venezia, Verona, Vicenza). You can see below where they are geographically located')

  st.map(df)

  st.title('Legend')
  st.write('I did not want to change the names of the descriptive variables in my dataframe as they are very similar to English words, and therefore understandable. It can also be a good way to learn some Italian words!')
  st.markdown("""However, here is the list of all the Analyzed variables (translated from Italian to English):

  ## Location Data
  - Provincia = Province 
  - Comune = municipality
  - Centro Storico = Historical Centre
  - Zona Fiera = Exhibition Area
  - Lago = Lake
  - Aereoporto = Airport
  - Autostrada = Highway
  - Impianti di Risalita = Lifts (Ski)
  - Stazione FS = Railway Station
  - Mare = Sea
  - Termale = Thermal Area

  ## Services
  - Piscina = Swimming Pool
  - Ristorante = Restaurant
  - Parcheggio = Parking Spots
  - Aria Condizionata = Air Conditioning 
  - Giochi Bimbi = Children Games
  - Sauna = Sauna
  - Fitness = Fitness
  - Animali Ammessi = Pet Allowed
  - Inglese = English (Speaking)
  - Tedesco = German (Speaking)
  - Francese = French (Speaking)
  - Spagnolo = Spanish (Speaking)
  - Chiusura Temporanea = Temporary Closure
  """)

## CLEAN FOR CORRELATION AND MODEL

## under 3, over 3, over 4 TR
## back to tourism_strustures_df

tourism_df_to_drop = tourism_structures_df.copy()

## drop the useless columns 
tourism_df_ok = tourism_df_to_drop.drop(tourism_df_to_drop.columns[[2,4,6,7,8,9,10,11,12,13,14,16,19,20,21,23,26,27,28,29,30,31,32,33,34,35,36,42,43]], axis=1)

## drop the Nan in classification column
nan_mask = tourism_df_ok['CLASSIFICAZIONE'].isnull()
tr_ok_clear_class_df = tourism_df_ok[nan_mask == False]

## new indexes for the dataframe

new_indexes = []

for i in range(len(tr_ok_clear_class_df)):
  new_indexes.append(i)

tr_ok_clear_class_df.index = new_indexes

## change classification data, from string to int

for i in range(len(tr_ok_clear_class_df)):
  if tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '1 *':
    tr_ok_clear_class_df.loc[i, 'CLASSIFICAZIONE'] = int(1)
  elif tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '2 **' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '2 Leoni':
    tr_ok_clear_class_df.loc[i, 'CLASSIFICAZIONE'] = int(2)
  elif tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '3 ***' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '3 Leoni' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '3 *** SUPERIOR':
    tr_ok_clear_class_df.loc[i, 'CLASSIFICAZIONE'] = int(3)
  elif tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '4 ****' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '4 Leoni' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '4 **** SUPERIOR':
    tr_ok_clear_class_df.loc[i, 'CLASSIFICAZIONE'] = int(4)
  elif tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '5 *****' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '5 Leoni' or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == '5 ***** lusso':
    tr_ok_clear_class_df.loc[i, 'CLASSIFICAZIONE'] = int(5)

## create new columns
under_3_class = []

for i in range(len(tr_ok_clear_class_df)):
  if tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 1 or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 2 :
    under_3_class.append(int(1))
  else:
    under_3_class.append(int(0))

class_3_4_5 = []

for i in range(len(tr_ok_clear_class_df)):
  if tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 3 or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 4 or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 5 :
    class_3_4_5.append(int(1))
  else:
    class_3_4_5.append(int(0))

class_4_5 = []

for i in range(len(tr_ok_clear_class_df)):
  if tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 4 or tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 5 :
    class_4_5.append(int(1))
  else:
    class_4_5.append(int(0))

class_5 = []

for i in range(len(tr_ok_clear_class_df)):
  if tr_ok_clear_class_df['CLASSIFICAZIONE'][i] == 5 :
    class_5.append(int(1))
  else:
    class_5.append(int(0))


tr_ok_clear_class_df['UNDER 3'] = under_3_class
tr_ok_clear_class_df['G.E 3'] = class_3
tr_ok_clear_class_df['G.E. 4'] = class_4
tr_ok_clear_class_df['CLASS 5'] = class_5

## new df
tr_df = tr_ok_clear_class_df
code_ok_df ='''
Int64Index: 7337 entries, 0 to 7336
Data columns (total 20 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   PROVINCIA             7337 non-null   object
 1   COMUNE                7337 non-null   object
 2   TIPOLOGIA             7337 non-null   object
 3   DENOMINAZIONE         7337 non-null   object
 4   PISCINA               7337 non-null   int64 
 5   RISTORANTE            7337 non-null   int64 
 6   PARCHEGGIO            7337 non-null   int64 
 7   SAUNA                 7337 non-null   int64 
 8   FITNESS               7337 non-null   int64 
 9   ANIMALI AMMESSI       7337 non-null   int64 
 10  INGLESE               7337 non-null   int64 
 11  FRANCESE              7337 non-null   int64 
 12  TEDESCO               7337 non-null   int64 
 13  SPAGNOLO              7337 non-null   int64 
 14  CHIUSURA TEMPORANEA   7337 non-null   int64 
 15  CLASSIFICAZIONE       7337 non-null   object
 16  UNDER 3               7337 non-null   int64 
 17  G.E 3                 7337 non-null   int64 
 18  G.E. 4                7337 non-null   int64 
 19  CLASS 5               7337 non-null   int64 
dtypes: int64(15), object(5)
'''

## create a groupby mean and sum by PROVINCIA

tr_groupby_mean = tr_df.groupby(['PROVINCIA']).mean()

tr_groupby_sum = tr_df.groupby(['PROVINCIA']).sum()





if st.sidebar.checkbox("EDA"):

    st.title('Explore and Clean the Dataset')

    st.write('**Note! throughout the project I will use the acronym TR to indicate the Tourist Residences in Veneto**')

    st.write('Firstly, I import the dataset using pandas. That is how it looks like:')

    st.dataframe(tourism_structures_df)

    st.write('Information about the original dataset:')

    st.code(code_original_info)

    st.header('What can I understand?')
    st.write('As I can see, the dataset have 45 columns and 8504 rows.')
    st.write('The data are for the majority composed by objects(43), with string values!')
    st.write('Since I want to analyze the characteristics of the tourist residences, I need to trensform all the data with string values to boolean values 1 (True = Vero) and 0 (False = Falso)')
    st.write('I can use the map function')

    st.code(code_map)
    st.write('Info of the adjusted DF')
    st.code(code_adj_info)

    st.write('Now I have the adjusted descriptive characteristics.')
    
    st.header("""Let's Clean up the Dataset!""")

    st.write('Since, as I can see from information of DF, there are some problematic columns, I create a copy of the original dataframe in order to drop the ones that I will not use in my analysis.**_Problematic_** since they have unfixable null values.')

    st.write('The dropped columns are: **LOCATION, SECONDARY TYPE, ADDRESS, HOUSE NUMBER, INTERNAL, ZIP CODE, PHONE, FAX, EMAIL ADDRESS, WEBSITE, AREA, LAST EDIT, IDENTIFICATION CODE**.')
    st.write('These columns provide __useless__ information, since they concern only the single residential facility, and are linked to **contact information**. ')

    st.markdown("""I also drop the following columns that, even if they provide descriptive informations, are not relevant for my purposes:
     - **INDOOR SWIMMING POOL**, 
     - **CONFERENCE ROOM**, 
     - **SOLARIUM**, 
     - **OUTSKIRTS**, 
     - **HILLS**""")

    st.write('__Info of the Cleaned DF__')
    st.code(code_cleaned_df)

    st.title('Change the classification')

    st.write('Since the classification of the tourist residences is an object column fill with all the classification rates, I want to split these values in different columns, which will have boolean values 1 and 0 depending on the classification of the TR ')
    
    st.write('These are the values inside the classification column (using the .unique() function):')
    st.code(code_class_unique)
    
    st.write('That is the DF with new columns for the different classifications (swipe right):')
    st.dataframe(tourism_clear_class_df)
    
    st.title('.Groupby([PROVINCIA])')
    st.header('Info about Average (.mean()) and Total Number (.sum()) of TR with **descriptive variable** by Provincia')
    st.write('The following dataframe gives me info about the average and total number of accomodations with certain characteristics:')
    st.header('__AVERAGE__')

    st.dataframe(tourism_clear_class_groupby_mean.T)

    st.header('__TOTAL BY PROVINCIA__')

    st.dataframe(tourism_clear_class_groupby_sum.T)

    st.write('The cleaning and modifications made so far were necessary for plotting the graphs that can be seen in the section **PLOTS**. Later I took the original file and modified it to make it ready for analysis with heatmap and correlation')

    st.title('CLEANINIG FOR CORRELATION AND HEATMAP')

    st.write('This is the dataset with only the columns I will use for the correlation.')
    st.dataframe(tr_ok_clear_class_df)

    st.write('These are the info of my new DF:')
    st.code(code_ok_df)

    st.write('The **HEATMAP AND CORRELATION** section show the correlation DF and Heatmap')


## PLOTS

province = [
    'BELLUNO',
    'PADOVA',
    'TREVISO',
    'ROVIGO',
    'VENEZIA',
    'VERONA',
    'VICENZA'
]

## which provincia has the higher number of TR?

plt.figure(figsize=(10,10))
plt.title('TR by Provincia')
for i in range(len(city_list)):
  plt.bar(province[i], city_len[i])
  plt.text(province[i], city_len[i], str(city_len[i]), ha='center', weight='bold')


## PET-FRIENDLY
## Definition of PET Friendly:
## Animal friendly tourist residences are accommodations that are:
## designed and managed to be welcoming and accommodating to both human guests and their animal companions.
## This may include features such as designated pet-friendly rooms or areas, 
## easy access to outdoor spaces for exercise and relief, and possibly even on-site pet services such as grooming or boarding.
# ## animal friendly pie charts


## 1 normalizing the number of animal-friendly tr

belluno_af_tr = belluno_descriptive.loc['ANIMALI AMMESSI']
padova_af_tr = padova_descriptive.loc['ANIMALI AMMESSI']
treviso_af_tr = treviso_descriptive.loc['ANIMALI AMMESSI']
rovigo_af_tr = rovigo_descriptive.loc['ANIMALI AMMESSI']
venezia_af_tr = venezia_descriptive.loc['ANIMALI AMMESSI']
verona_af_tr = verona_descriptive.loc['ANIMALI AMMESSI']
vicenza_af_tr = vicenza_descriptive.loc['ANIMALI AMMESSI']

af_array_1 = np.array([belluno_af_tr/belluno_tr, padova_af_tr/padova_tr, treviso_af_tr/treviso_tr, rovigo_af_tr/rovigo_tr, venezia_af_tr/venezia_tr, verona_af_tr/verona_tr, vicenza_af_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(af_array_1[np.newaxis])

af_array_2 = np.array([belluno_af_tr, padova_af_tr, treviso_af_tr, rovigo_af_tr, venezia_af_tr, verona_af_tr, vicenza_af_tr])
normalized_arr_2 = preprocessing.normalize(af_array_2[np.newaxis])

fig1, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of Pet-Friendly TR", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of Pet-Friendly TR", fontweight='bold')

fig1.suptitle("Pet-Friendly TR in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

animal_friendly_list=[belluno_af_tr, padova_af_tr, treviso_af_tr, rovigo_af_tr, venezia_af_tr, verona_af_tr, vicenza_af_tr]

fig2, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many Pet-Friendly TR are in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(animal_friendly_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], animal_friendly_list[i], color='orange', width = 0.5, label='Animal Friendly TR')
    number=round((animal_friendly_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], animal_friendly_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

list_of_colors=[
'red',
'blue',
'green',
'cyan',
'magenta',
'yellow',
'pink']

data = [city_len, animal_friendly_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((animal_friendly_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences are pet friendly in Veneto?

sum_pf = np.sum(animal_friendly_list)
total_tr = np.sum(city_len)

## ratio of animal friendly tr in Veneto

ratio_af_tr = sum_pf/total_tr

## create a pie chart with the pf tourist residences and the not pf tourist residences in Veneto

labels = ['Pet Friendly', 'Not Pet Friendly']
sizes = [ratio_af_tr, 1 - ratio_af_tr]

fig3, ax1 = plt.subplots(figsize=(10,10))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Pet Friendly Tourist Residences in Veneto", fontsize=20)



## POOL


belluno_pool_tr = belluno_descriptive.loc['PISCINA']
padova_pool_tr = padova_descriptive.loc['PISCINA']
treviso_pool_tr = treviso_descriptive.loc['PISCINA']
rovigo_pool_tr = rovigo_descriptive.loc['PISCINA']
venezia_pool_tr = venezia_descriptive.loc['PISCINA']
verona_pool_tr = verona_descriptive.loc['PISCINA']
vicenza_pool_tr = vicenza_descriptive.loc['PISCINA']

## array with ratio of pool tr and total tr by provincia
pool_array_1 = np.array([belluno_pool_tr/belluno_tr, padova_pool_tr/padova_tr, treviso_pool_tr/treviso_tr, rovigo_pool_tr/rovigo_tr, venezia_pool_tr/venezia_tr, verona_pool_tr/verona_tr, vicenza_pool_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(pool_array_1[np.newaxis])

## array with number of pool tr by provincia
pool_array_2 = np.array([belluno_pool_tr, padova_pool_tr, treviso_pool_tr, rovigo_pool_tr, venezia_pool_tr, verona_pool_tr, vicenza_pool_tr])
normalized_arr_2 = preprocessing.normalize(pool_array_2[np.newaxis])

## create pie charts
fig4, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")


## normalizing tha array
## In this way i will have an array with normalized values for the two data
data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[0] --> this is the one in which I see the normalizet proportion of TR with Pool by provincia
axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of TR with Pool", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[1] --> this is the axs in which I see the normalized proportion of TR with Pool in Veneto (Total number of TR with Pool)
axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of TR with Pool", fontweight='bold')

fig4.suptitle(" TR with Pool in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

pool_list=[belluno_pool_tr, padova_pool_tr, treviso_pool_tr, rovigo_pool_tr, venezia_pool_tr, verona_pool_tr, vicenza_pool_tr]

fig5, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many TR have Pool in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(pool_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], pool_list[i], color='orange', width = 0.5, label='TR with Pool')
    number=round((pool_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], pool_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

data = [city_len, pool_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((pool_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences have Pool in Veneto?

sum_pool = np.sum(pool_list)
total_tr = np.sum(city_len)

ratio_pool_tr = sum_pool/total_tr

labels = ['With Pool', 'Without Pool']
sizes = [ratio_pool_tr, 1 - ratio_pool_tr]

fig6, ax1 = plt.subplots(figsize=(10,8))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Tourist Residences with Pool in Veneto", fontsize=20)


## ENGLISH 
## Definition of English:
## Tourist residences that speak English refer to accomodations where the staff or management can communicate effectively in English with the guests.
## These types of properties are popular among tourists and vacationers who primarily speak English and may not be fluent in the local language. 
## This can include properties where the front-desk staff, housekeeping, maintenance, and other staff members are able to speak and understand English, as well as properties where the majority of guests are English-speaking. 
## Some tourist residences may also provide written information or signage in English to help guests navigate their stay. 
## These type of tourist residences are a great option for travelers who are visiting a foreign country and want to feel comfortable and well-informed during their stay.

belluno_eng_tr = belluno_descriptive.loc['INGLESE']
padova_eng_tr = padova_descriptive.loc['INGLESE']
treviso_eng_tr = treviso_descriptive.loc['INGLESE']
rovigo_eng_tr = rovigo_descriptive.loc['INGLESE']
venezia_eng_tr = venezia_descriptive.loc['INGLESE']
verona_eng_tr = verona_descriptive.loc['INGLESE']
vicenza_eng_tr = vicenza_descriptive.loc['INGLESE']

## array with ratio of English Speaking TR
eng_array_1 = np.array([belluno_eng_tr/belluno_tr, padova_eng_tr/padova_tr, treviso_eng_tr/treviso_tr, rovigo_eng_tr/rovigo_tr, venezia_eng_tr/venezia_tr, verona_eng_tr/verona_tr, vicenza_eng_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(eng_array_1[np.newaxis])

## array with number of English Speaking TR
eng_array_2 = np.array([belluno_eng_tr, padova_eng_tr, treviso_eng_tr, rovigo_eng_tr, venezia_eng_tr, verona_eng_tr, vicenza_eng_tr])
normalized_arr_2 = preprocessing.normalize(eng_array_2[np.newaxis])

## create pie charts
fig7, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")


## normalizing tha array
## In this way i will have an array with normalized values for the two data
data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[0] --> this is the one in which I see the normalizet proportion of TR with Pool by provincia
axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of TR speaking English ", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[1] --> this is the axs in which I see the normalized proportion of TR 
axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of TR speaking English ", fontweight='bold')

fig7.suptitle("TR speaking English in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

eng_list=[belluno_eng_tr, padova_eng_tr, treviso_eng_tr, rovigo_eng_tr, venezia_eng_tr, verona_eng_tr, vicenza_eng_tr]

fig8, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many TR speak English in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(eng_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], eng_list[i], color='orange', width = 0.5, label='TR speaking English')
    number=round((eng_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], eng_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

data = [city_len, eng_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((eng_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences speak English in Veneto?

sum_eng = np.sum(eng_list)
total_tr = np.sum(city_len)

## ratio in Veneto

ratio_eng_tr = sum_eng/total_tr

## create a pie chart 

labels = ['Do Speak English', 'Do Not Speak English']
sizes = [ratio_eng_tr, 1 - ratio_eng_tr]

fig9, ax1 = plt.subplots(figsize=(10,7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Tourist Residences Speak English in Veneto", fontsize=20)


## ALL FOUR LANGUAGES (ENGLISH, SPANISH, GERMAN, FRENCH)
## Definition of 4 Languages
##Tourist residences that speak English, Spanish, German, French refer to accomodations where the staff or management can communicate effectively in multiple languages,
## including English, Spanish, German, and French with the guests. 

belluno_lan_tr = belluno_descriptive.loc['LANGUAGES']
padova_lan_tr = padova_descriptive.loc['LANGUAGES']
treviso_lan_tr = treviso_descriptive.loc['LANGUAGES']
rovigo_lan_tr = rovigo_descriptive.loc['LANGUAGES']
venezia_lan_tr = venezia_descriptive.loc['LANGUAGES']
verona_lan_tr = verona_descriptive.loc['LANGUAGES']
vicenza_lan_tr = vicenza_descriptive.loc['LANGUAGES']


lan_array_1 = np.array([belluno_lan_tr/belluno_tr, padova_lan_tr/padova_tr, treviso_lan_tr/treviso_tr, rovigo_lan_tr/rovigo_tr, venezia_lan_tr/venezia_tr, verona_lan_tr/verona_tr, vicenza_lan_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(lan_array_1[np.newaxis])


lan_array_2 = np.array([belluno_lan_tr, padova_lan_tr, treviso_lan_tr, rovigo_lan_tr, venezia_lan_tr, verona_lan_tr, vicenza_lan_tr])
normalized_arr_2 = preprocessing.normalize(lan_array_2[np.newaxis])

## create pie charts
fig10, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")


## normalizing tha array
## In this way i will have an array with normalized values for the two data
data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[0] --> this is the one in which I see the normalizet proportion of TR 
axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of TR speaking All Languages ", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[1] --> this is the axs in which I see the normalized proportion of TR that speak all 4 lenguages in Veneto
axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of TR speaking All Languages ", fontweight='bold')

fig10.suptitle("TR speaking all Languages in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

lan_list=[belluno_lan_tr, padova_lan_tr, treviso_lan_tr, rovigo_lan_tr, venezia_lan_tr, verona_lan_tr, vicenza_lan_tr]

fig11, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many TR speak All Languages in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(lan_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], lan_list[i], color='orange', width = 0.5, label='TR speaking All Languages')
    number=round((lan_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], lan_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

data = [city_len, lan_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((lan_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences speak All Languages in Veneto?

sum_lan = np.sum(lan_list)
total_tr = np.sum(city_len)

ratio_lan_tr = sum_lan/total_tr

labels = ['Do Speak All Languages', 'Do Not Speak All Languages']
sizes = [ratio_lan_tr, 1 - ratio_lan_tr]

fig12, ax1 = plt.subplots(figsize=(10,7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Tourist Residences Speak All Languages in Veneto", fontsize=20)


## Parking
## Tourist residences with private parking are accomodations that provide private parking spaces for guests.
## The private parking is a convenience for guests who have rented a vehicle or brought their own, as it provides a secure and convenient place to park.

belluno_park_tr = belluno_descriptive.loc['PARCHEGGIO']
padova_park_tr = padova_descriptive.loc['PARCHEGGIO']
treviso_park_tr = treviso_descriptive.loc['PARCHEGGIO']
rovigo_park_tr = rovigo_descriptive.loc['PARCHEGGIO']
venezia_park_tr = venezia_descriptive.loc['PARCHEGGIO']
verona_park_tr = verona_descriptive.loc['PARCHEGGIO']
vicenza_park_tr = vicenza_descriptive.loc['PARCHEGGIO']

## array with ratio of pool tr and total tr by provincia
park_array_1 = np.array([belluno_park_tr/belluno_tr, padova_park_tr/padova_tr, treviso_park_tr/treviso_tr, rovigo_park_tr/rovigo_tr, venezia_park_tr/venezia_tr, verona_park_tr/verona_tr, vicenza_park_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(park_array_1[np.newaxis])

## array with number of pool tr by provincia
park_array_2 = np.array([belluno_park_tr, padova_park_tr, treviso_park_tr, rovigo_park_tr, venezia_park_tr, verona_park_tr, vicenza_park_tr])
normalized_arr_2 = preprocessing.normalize(park_array_2[np.newaxis])

## create pie charts
fig13, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")


## normalizing tha array
## In this way i will have an array with normalized values for the two data
data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[0] --> this is the one in which I see the normalizet proportion of TR with Parking by provincia
axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of TR with Private Parking ", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[1] --> this is the axs in which I see the normalized proportion of TR with Parking in Veneto
axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of TR with Private Parking ", fontweight='bold')

fig13.suptitle("TR with Private Parking in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

park_list=[belluno_park_tr, padova_park_tr, treviso_park_tr, rovigo_park_tr, venezia_park_tr, verona_park_tr, vicenza_park_tr]

fig14, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many TR have Private Parking in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(park_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], park_list[i], color='orange', width = 0.5, label='TR with PP')
    number=round((park_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], park_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

data = [city_len, park_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((park_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences have Private Parking in Veneto?

sum_park = np.sum(park_list)
total_tr = np.sum(city_len)

ratio_park_tr = sum_park/total_tr

labels = ['Do Have Private Parking', 'Do Not Have Private Parking']
sizes = [ratio_park_tr, 1 - ratio_park_tr]

fig15, ax1 = plt.subplots(figsize=(10,7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Tourist Residences Speak All Languages in Veneto", fontsize=20)

## RESTAURANT
## Definition of Restaurant:
## Tourist residences with a restaurant refers to accomodations that have an on-site restaurant. 
## These types of properties are popular among tourists and vacationers who are looking for a place to stay that offers the convenience of having a restaurant where they can enjoy meals during their stay.
## The restaurant can be a shared space, or a private space that is only accessible to guests staying in the residence.


belluno_rest_tr = belluno_descriptive.loc['RISTORANTE']
padova_rest_tr = padova_descriptive.loc['RISTORANTE']
treviso_rest_tr = treviso_descriptive.loc['RISTORANTE']
rovigo_rest_tr = rovigo_descriptive.loc['RISTORANTE']
venezia_rest_tr = venezia_descriptive.loc['RISTORANTE']
verona_rest_tr = verona_descriptive.loc['RISTORANTE']
vicenza_rest_tr = vicenza_descriptive.loc['RISTORANTE']

## array with ratio of tr with restaurant and total tr by provincia
rest_array_1 = np.array([belluno_rest_tr/belluno_tr, padova_rest_tr/padova_tr, treviso_rest_tr/treviso_tr, rovigo_rest_tr/rovigo_tr, venezia_rest_tr/venezia_tr, verona_rest_tr/verona_tr, vicenza_rest_tr/vicenza_tr])
normalized_arr_1 = preprocessing.normalize(rest_array_1[np.newaxis])

## array with number of tr with restaurant by provincia
rest_array_2 = np.array([belluno_rest_tr, padova_rest_tr, treviso_rest_tr, rovigo_rest_tr, venezia_rest_tr, verona_rest_tr, vicenza_rest_tr])
normalized_arr_2 = preprocessing.normalize(rest_array_2[np.newaxis])

## create pie charts
fig16, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10), constrained_layout = True)
palette = sb.color_palette("pastel")


## normalizing tha array
## In this way i will have an array with normalized values for the two data
data_1 = (normalized_arr_1.T).flatten()
data_2 = (normalized_arr_2.T).flatten()

labels = province

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[0] --> this is the one in which I see the normalizet proportion of TR with Restaurant by provincia
axs[0].pie(data_1, autopct='%.2f%%', labels =labels, colors =palette)
axs[0].add_artist(donut_circle)
axs[0].set_title("Normalized Proportion of TR with Restaurant ", fontweight='bold')

donut_circle = plt.Circle( (0,0), 0.45, color = 'white')

## axs[1] --> this is the axs in which I see the normalized proportion of TR with restaurant in Veneto (Total number of TR with Restaurant)
axs[1].pie(data_2, autopct='%.2f%%', colors =palette)
axs[1].add_artist(donut_circle)
axs[1].set_title("Not Normalized Proportion of TR with Restaurant ", fontweight='bold')

fig16.suptitle(" TR with Restaurant in Veneto", fontsize=30)

plt.legend(labels, title='Province')
plt.axis('equal')

rest_list=[belluno_rest_tr, padova_rest_tr, treviso_rest_tr, rovigo_rest_tr, venezia_rest_tr, verona_rest_tr, vicenza_rest_tr]

## Stacked Bar Chart

fig17, axs = plt.subplots(1, 2, figsize=(30, 10))

plt.suptitle('How many TR have Restaurant in Veneto?', fontsize=25.9)

axs[0].set_title('Stacked Bar Chart', fontsize=20)
axs[0].set_xlabel('Province')
axs[0].set_ylabel('Number of Tourist Residences')

for i in range(len(rest_list)):
    axs[0].bar(province[i], city_len[i], color='grey', width = 0.5, label='Total TR')
    axs[0].bar(province[i], rest_list[i], color='orange', width = 0.5, label='TR with Restaurant')
    number=round((rest_list[i]/city_len[i])*100,1)
    axs[0].text(province[i], rest_list[i], str(number)+'%', ha='center',va= 'bottom', weight='bold')

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[0].legend(by_label.values(), by_label.keys())

## 2nd bar chart ( multiple bar chart)

X=np.arange(7)

data = [city_len, rest_list]

axs[1].set_title('Multiple Bar Chart',fontsize=20)
axs[1].set_xlabel('Province')
axs[1].set_ylabel('Number of Tourist Residences')

for i in X:
    axs[1].bar(X[i] - 0.15, data[1][i], width = 0.25, color = list_of_colors[i])
    axs[1].bar(X[i] + 0.15, data[0][i], color = 'grey', width = 0.25, label='Total TR')
    number=round((rest_list[i]))
    axs[1].text(X[i] - 0.15, data[1][i], str(number), ha='center',va= 'bottom', weight='bold')
    number=round((city_len[i]))
    axs[1].text(X[i] + 0.15, data[0][i], str(number), ha='center',va= 'bottom', weight='bold')
    

# the following 3 lines are only to avoid legend repetition
handles, labels = axs[1].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axs[1].legend(by_label.values(), by_label.keys())

## set the name of province in x axis
axs[1].set_xticks(X)
axs[1].set_xticklabels(province)

## How many tourist residences have Restaurant in Veneto?

sum_rest = np.sum(rest_list)
total_tr = np.sum(city_len)

## ratio of tr with restaurant in Veneto

ratio_rest_tr = sum_rest/total_tr

## create a pie chart with the tourist residences with restaurant and without in Veneto

labels = ['With Restaurant', 'Without Restaurant']
sizes = [ratio_rest_tr, 1 - ratio_rest_tr]

fig18, ax1 = plt.subplots(figsize=(10,7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=palette)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.suptitle("Tourist Residences with Restaurant in Veneto", fontsize=20)

plt.show()

if st.sidebar.checkbox("PLOTS"):

    st.title('PLOTS')  
    st.write('In this section you will find PLOTS refering to the analysis of the TR characteristics.')

    ## which provincia has the higher number of TR?

    
    st.title("City Lengths by Province")

    len_prov = {'BELLUNO':825, 'PADOVA':553, 'TREVISO':555, 'ROVIGO':178, 'VENEZIA':2570, 'VERONA':2024, 'VICENZA':632}
    len_prov = pd.Series(len_prov)
    len_prov_df = pd.DataFrame(len_prov)
    len_prov_df.columns = ['# TR']

    st.bar_chart(len_prov_df)

    st.title('Analyze the Province')
    st.write('__Now__, you can see the full analysis of TR by Provincia in the two plots below.')
    st.write('The __former__ is a bar chart with the information of the number of TR in the chosen Provincia with the particular characteristic.')
    st.write('The __latter__ refers to the percentage of TR with the presence of the particular characteristic.')
    
    city = st.selectbox("__What Provincia do you want to analyze?__", province)

    plt.figure(figsize=(30,10))

    if city == 'BELLUNO':

        st.title('How many TR in Belluno have...(numbers)?')    
        st.bar_chart(belluno_descriptive)
   
        st.title('How many TR in Belluno have...(%)?')
        plt.title('Informations of TR in Belluno', fontsize= 20)
        plt.bar('Total', city_len[0])

        for i in range(len(belluno_descriptive)):
            plt.bar(belluno_descriptive.index[i], belluno_descriptive[i])
            plt.xticks(rotation=45)
            number = round((belluno_descriptive[i]/belluno_tr)*100,1)
            plt.text(belluno_descriptive.index[i], belluno_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
  

    elif city == 'PADOVA':

        st.title('How many TR in Padova have...(numbers)?')
        st.bar_chart(padova_descriptive)

        st.title('How many TR in Padova have...(%)?')
        plt.title('Informations of TR in Padova', fontsize= 20)
        plt.bar('Total', city_len[1])
        for i in range(len(padova_descriptive)):
            plt.bar(padova_descriptive.index[i], padova_descriptive[i])
            plt.xticks(rotation=45)
            number = round((padova_descriptive[i]/padova_tr)*100,1)
            plt.text(padova_descriptive.index[i], padova_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
  

    elif city == 'TREVISO':

        st.title('How many TR in Treviso have...(numbers)?')
        st.bar_chart(treviso_descriptive)
        st.title('How many TR in Treviso have...(%)?')
        plt.title('Informations of TR in Treviso', fontsize= 20)
        plt.bar('Total', city_len[2])
        for i in range(len(treviso_descriptive)):
            plt.bar(treviso_descriptive.index[i], treviso_descriptive[i])
            plt.xticks(rotation=45)
            number = round((treviso_descriptive[i]/treviso_tr)*100,1)
            plt.text(treviso_descriptive.index[i], treviso_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
  
    
    elif city == 'ROVIGO':
        st.title('How many TR in Rovigo have...(numbers)?')
        st.bar_chart(rovigo_descriptive)
        st.title('How many TR in Rovigo have...(%)?')
        plt.title('Informations of TR in Rovigo', fontsize= 20)
        plt.bar('Total', city_len[3])
        
        for i in range(len(rovigo_descriptive)):
            plt.bar(rovigo_descriptive.index[i], rovigo_descriptive[i])
            plt.xticks(rotation=45)
            number = round((rovigo_descriptive[i]/rovigo_tr)*100,1)
            plt.text(rovigo_descriptive.index[i], rovigo_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
    

    elif city == 'VENEZIA':

        st.title('How many TR in Venezia have...(numbers)?')
        st.bar_chart(venezia_descriptive)
        st.title('How many TR in Venezia have...(%)?')
        plt.title('Informations of TR in Venezia(%)', fontsize= 20)
        plt.bar('Total', city_len[4])
        for i in range(len(venezia_descriptive)):
            plt.bar(venezia_descriptive.index[i], venezia_descriptive[i])
            plt.xticks(rotation=45)
            number = round((venezia_descriptive[i]/venezia_tr)*100,1)
            plt.text(venezia_descriptive.index[i], venezia_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
    

    elif city == 'VERONA':
        
        st.title('How many TR in Verona have...(numbers)?')
        st.bar_chart(verona_descriptive)

        st.title('How many TR in Verona have...(%)?')
        
        plt.title('Informations of TR in Verona(%)', fontsize= 20)
        plt.bar('Total', city_len[5])
        for i in range(len(verona_descriptive)):
            plt.bar(verona_descriptive.index[i], verona_descriptive[i])
            plt.xticks(rotation=45)
            number = round((verona_descriptive[i]/verona_tr)*100,1)
            plt.text(verona_descriptive.index[i], verona_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
   

    elif city == 'VICENZA':
        st.title('How many TR in Vicenza have...(numbers)?')
        st.bar_chart(vicenza_descriptive)
        st.title('How many TR in Vicenza have...(%)?')
        plt.title('Informations of TR in Vicenza', fontsize= 20)
        plt.bar('Total', city_len[6])
        for i in range(len(vicenza_descriptive)):
             plt.bar(vicenza_descriptive.index[i], vicenza_descriptive[i])
             plt.xticks(rotation=45)
             number = round((vicenza_descriptive[i]/vicenza_tr)*100,1)
             plt.text(vicenza_descriptive.index[i], vicenza_descriptive[i], str(number)+'%', ha='center', weight='bold')
        st.pyplot(plt.gcf())
    
    st.title('TR Characteristic Analysis')
    plot = st.selectbox('__Choose the Variable to Analyze__',('Pet-friendly TR','TR with Pool','TR that speak foreign language(s)','TR with Private Parking Spots','TR with Restaurant'))


    if plot == 'Pet-friendly TR':
      st.title('Pet-Friendly TR in Veneto')
     
      st.write('Pet-friendly tourist residences are accommodations that are designed and managed to be welcoming and accommodating to both human guests and their animal companions. This may include features such as designated pet-friendly rooms or areas, easy access to outdoor spaces for exercise and relief, and possibly even on-site pet services such as grooming or boarding.')
      st.write('The __first__ pie chart refers to the number of Pet-friendly TR normalized by number of TR by Provincia. The __second__ refers to the total number of Pet-friendly TR in Veneto')
      st.subheader('Pie Charts')
      st.write(fig1)

      st.subheader('Bar Charts')
      st.write('These bar charts show the percentage (1) and the number (2) of Pet-friendly TR by Provincia')
      st.write(fig2)

      st.subheader('Portion of Pet-Frientdly TR in Veneto')
      st.write('How many TR are Pet-friendly?')
      st.write(fig3)

    if plot == 'TR with Pool':

      st.title('TR with Pool in Veneto')
      st.write('Tourist residences with pool refers to accomodation that have a swimming pool on the property. These types of properties are popular among tourists and vacationers who are looking for a place to stay that offers the convenience and luxury of having a pool to swim in during their stay. ')
      st.write('The __first__ pie chart refers to the number of TR with Pool normalized by number of TR by Provincia. The __second__ refers to the total number of TR with Pool in Veneto')
     

      st.subheader('Pie Charts')   
      st.write(fig4)

      st.subheader('Bar Charts')
      st.write('These bar charts show the percentage (1) and the number (2) of TR with Pool by Provincia')
      st.write(fig5)

      st.subheader('Portion of TR wirh Pool in Veneto')
      st.write('How many TR have Pool?')
      st.write(fig6)


    if plot == 'TR that speak foreign language(s)':
      st.title('Difference between English and All 4 Languages')
      st.write('The floolwing plots show the difference between English Speaking TR (the universal language) and TR that speak all 4 principal languages (***Spanish, German, French, English***.) ')
    
      st.subheader('Pie Chart')
      st.write('Pie charts showing the percentage of TR speaking foreign language(s) by provincia (Normalized) and in Veneto (Not Normalized)')
      st.write(fig7)
      st.write(fig10)

      st.subheader('Bar Charts')
      st.write('Bar charts show the percentage and number of TR speaking foreign language(s)')
      st.write(fig8)
      st.write(fig11)

      st.subheader('Portion of TR Speaking Foreign Language(s)')
      st.write('The two pie charts show how the two descriptive variables lead to opposite results in the number of tourist residences ')
      st.write(fig9)
      st.write(fig12)
    
    if plot == 'TR with Private Parking Spots':

      st.title('TR with Private Parking Spots')
      st.write('Tourist residences with private parking are accomodations that provide private parking spaces for guests. The private parking is a convenience for guests who have rented a vehicle or brought their own, as it provides a secure and convenient place to park.')

      st.subheader('Pie Charts')
      st.write('The __first__ pie chart refers to the number of TR with PP spots normalized by number of TR by Provincia. The __second__ refers to the total number of TR with PP spots in Veneto')   
      st.write(fig13)

      st.subheader('Bar Charts')
      st.write('These bar charts show the percentage (1) and the number (2) of TR with PP Spots by Provincia')
      st.write(fig14)

      st.subheader('Portion of TR wirh Pool in Veneto')
      st.write('How many TR have Private Parking Spots?')
      st.write(fig15)
    
    if plot == 'TR with Restaurant':
      st.title('TR with Restaurant')
      st.write('Tourist residences with a restaurant refers to accomodations that have an on-site restaurant. These types of properties are popular among tourists and vacationers who are looking for a place to stay that offers the convenience of having a restaurant where they can enjoy meals during their stay. The restaurant can be a shared space, or a private space that is only accessible to guests staying in the residence..')
      
      st.subheader('Pie Charts')
      st.write('The __first__ pie chart refers to the number of TR with Restaurant normalized by number of TR by Provincia. The __second__ refers to the total number of TR with Restaurant in Veneto')   
      st.write(fig16)

      st.subheader('Bar Charts')
      st.write('These bar charts show the percentage (1) and the number (2) of TR with Restaurant by Provincia')
      st.write(fig17)

      st.subheader('Portion of TR wirh Pool in Veneto')
      st.write('How many TR have Restaurant?')
      st.write(fig18)



## Correlation and Heatmap

## correlation df
tr_corr = tr_groupby_mean.corr()




if st.sidebar.checkbox("CORRELATION AND HEATMAP"):

  st.title('CORRELATION AND HEATMAP')

  st.write('In this section I show the correlation DF and the Heatmap')

  st.header('Correlation')
  st.write('This is the Correlation DF:')

  st.dataframe(tr_df.corr())

  ## heatmap 

  st.header("Heatmap")
  st.write("Here is a heatmap visualization:")
  fig16 = plt.figure(figsize=(20,12))
  sb.heatmap(tr_df.corr(), annot=True)

  st.write(fig16)

  st.write('The heatmap shows the correlation between two descriptive variables. The higher is the value of the correlation (the more near to 1 it is) the lighter is the color of the cell, and vice versa.')
  st.write('In the next section I try to build a linear regression model in order to study how the correlation changes as the classification of the tourist residence increases')


## MODEL
##  linear regression model

if st.sidebar.checkbox("MODEL"):

  st.title('Linear Regression Model')
  st.write('I want to find out the impact that the different descriptive variables have on classification.')
  st.write('How does the classification depend on the analyzed variables?')

  language=[]
  for i in range(len(tr_df)):
    if (tr_df['INGLESE'][i] == 1) & (tr_df['TEDESCO'][i] == 1) & (tr_df['SPAGNOLO'][i] == 1) & (tr_df['FRANCESE'][i] == 1) :
      language.append(1)
    else:
      language.append(0)

  tr_df['LANGUAGES'] = language


  y_under_3 = tr_df['UNDER 3']
  y_over_3 = tr_df['G.E 3']
  y_over_4 = tr_df['G.E. 4']
  y_5 = tr_df['CLASS 5']
  X = tr_df[['PISCINA',
       'RISTORANTE', 'PARCHEGGIO', 'SAUNA', 'FITNESS', 'ANIMALI AMMESSI',
       'INGLESE', 'LANGUAGES' ]]


  choose_class = st.selectbox('__Choose the Classification__',('Under 3 Classification TR','Greater Equal 3 Classification TR','Greater Equal 4 Classification TR','5 Class TR'))
  
  if choose_class == 'Under 3 Classification TR':

    reg=LinearRegression().fit(X,y_under_3)

  if choose_class == 'Greater Equal 3 Classification TR':

    reg=LinearRegression().fit(X,y_over_3)

  if choose_class == 'Greater Equal 4 Classification TR':

    reg=LinearRegression().fit(X,y_over_4)

  if choose_class == '5 Class TR':

    reg=LinearRegression().fit(X,y_5)
  
  intercept_label = ['intercept']
  coeff_df = pd.DataFrame([*intercept_label,*X.columns])
  coeff_df.columns = ['Predictors']
  coeff_df['Coefficients'] = [*[reg.intercept_], *reg.coef_]

  st.write(coeff_df)
