import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Touristic Residences in Veneto :lion_face:')
st.title('Nicolò Avesani VR490189, Final Project')

st.header('## 1 Explore and Clean the Dataset')

st.write('Firstly, I import the dataset using pandas. That is how it looks like:')

tourism_structures_df = pd.read_csv('https://www.veneto.eu/static/opendata/dove-alloggiare.csv')

st.dataframe(tourism_structures_df)

st.write('Information about the original dataset:')

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

st.code(code_original_info)

st.header('What can I understand?')
st.write('As I can see, the dataset have 45 columns and 8504 rows.')
st.write('The data are for the majority composed by objects(43), with string values!')
st.write('Since I want to analyze the characteristics of the touristic residences,')
st.write('I need to trensform all the data with string values to boolean values 1 (True = Vero) and 0 (False = Falso)')
st.write('I can use the map function')

code_map='''
for i in range(len(tourism_structures_df)):
  for j in tourism_structures_df.columns:
    if (tourism_structures_df[j][i] == 'Vero') | (tourism_structures_df[j][i] == 'Falso'):
      tourism_structures_df[j] = tourism_structures_df[j].map({'Vero':1,'Falso':0}) 
'''

st.code(code_map)
## Since the majority of data are string values, so I need to transform them into boolean values with 1 for True(Vero) and 0 for False (Falso)

for i in range(len(tourism_structures_df)):
  for j in tourism_structures_df.columns:
    if (tourism_structures_df[j][i] == 'Vero') | (tourism_structures_df[j][i] == 'Falso'):
      tourism_structures_df[j] = tourism_structures_df[j].map({'Vero':1,'Falso':0}) 

st.text('Info of the adjusted DF')
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

st.code(code_adj_info)

st.write('Now I have the descriptive characteristics adjusted.')
st.write('They tell me the mean of total touristic residences in Veneto with the index as characteristic ')

ts_desriptive_mean = tourism_structures_df.describe().T['mean']

st.dataframe(ts_desriptive_mean)

st.header('What about the Provincie?')

tr_groupby_mean = tourism_structures_df.groupby(['PROVINCIA']).mean()

st.write('Using groupby function, I can see the average number of TR with characteristics in column per Provincia')

st.dataframe(tr_groupby_mean)

## create a copy of the original dataframe in order to drop some problematic and useless columns that I will not use in my analysis.
## 'Problematic' since they have null values.

## The dropped columns are: LOCATION, SECONDARY TYPE, ADDRESS, HOUSE NUMBER, INTERNAL, ZIP CODE, PHONE, FAX, EMAIL ADDRESS, WEBSITE, AREA, LAST EDIT, IDENTIFICATION CODE.
## These columns provide useless information, since they concern only the single residential facility, and are linked to contact information. 
## The columns I am interested in are those which provide me information about the presence or not of descriptive characteristics of the touristic residences

## I also drop the following columns that, even if they provide information about descriptive characteristics, are not relevant for my purposes:
## INDOOR SWIMMING POOL, CONFERENCE ROOM, SOLARIUM, OUTSKIRTS, HILLS

st.header('Lets Clean up the Dataset!')

st.write('Since, as I can see from information of DF, there are some problematic columns,')
st.write('I create a copy of the original dataframe in order to drop these that I will not use in my analysis.')
st.write('**_Problematic_** since they have unfixable null values.')

st.write('The dropped columns are: LOCATION, SECONDARY TYPE, ADDRESS, HOUSE NUMBER, INTERNAL, ZIP CODE, PHONE, FAX, EMAIL ADDRESS, WEBSITE, AREA, LAST EDIT, IDENTIFICATION CODE.')
st.write('These columns provide useless information, since they concern only the single residential facility, and are linked to contact information. ')

st.write('I also drop the following columns that, even if they provide information about descriptive characteristics, are not relevant for my purposes: INDOOR SWIMMING POOL, CONFERENCE ROOM, SOLARIUM, OUTSKIRTS, HILLS')

tourism_df = tourism_structures_df.copy()

tourism_df = tourism_df.drop(tourism_df.columns[[2,4,6,7,8,9,10,11,12,13,14,16,19,23,35,36,42,43]],axis=1)

st.write('__There we go with the info of the Cleaned DF__')

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

st.code(code_cleaned_df)

st.header('Change the classificaion')

st.write('Since the classification of the touristic residences is an object column fill with all the single touristic residence classification rates, I want to split these values in different columns, which have boolean values 1 and 0 depending on the classification of the TR ')

## firstly, I must drop the null values rows and change the indexes

classification_nan_mask = tourism_df['CLASSIFICAZIONE'].isnull()
tourism_clear_class_df = tourism_df[classification_nan_mask == False]

new_indexes = []
for i in range(len(tourism_clear_class_df)):
    new_indexes.append(i)

tourism_clear_class_df.index = new_indexes

st.write('These are the values inside the classification column (using the .unique() function):')

code_class_unique = '''array(['1 *', '2 **', '2 Leoni', '3 ***', '3 *** SUPERIOR', '3 Leoni',
       '4 ****', '4 **** SUPERIOR', '4 Leoni', '5 *****', '5 ***** lusso',
       '5 Leoni'], dtype=object)'''

st.code(code_class_unique)

## I create new columns relative to different class of touristic residences


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


## I also create an all lenguages column in which I will have 1 if the touristic residence speak all 4 lenguages

languages = []

for i in range(len(tourism_clear_class_df)):
    if (tourism_clear_class_df.loc[i, 'INGLESE'] == 1) & (tourism_clear_class_df.loc[i, 'TEDESCO'] == 1) & (tourism_clear_class_df.loc[i, 'FRANCESE'] == 1) & (tourism_clear_class_df.loc[i, 'SPAGNOLO'] == 1):
        languages.append(1)
    else:
        languages.append(0)

tourism_clear_class_df['LANGUAGES'] = languages

st.write('That is the DF with new columns for the different classifications:')
st.dataframe(tourism_clear_class_df)

st.header('Info about Avarage and Total Number of TR per Provincia')
st.write('The following dataframe gives me info about the avarage and total number of accomodations with certain characteristics:')
st.write('__AVARAGE__')

tourism_clear_class_groupby_mean = tourism_clear_class_df.groupby(['PROVINCIA']).mean()

st.dataframe(tourism_clear_class_groupby_mean.T)

st.write('__TOTAL PER PROVINCIA__')

## Now I can understand how many touristic residences per provincia has the characteristics in index

tourism_clear_class_groupby_sum = tourism_clear_class_df.groupby(['PROVINCIA']).sum()

st.dataframe(tourism_clear_class_groupby_sum.T)

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

## length of the dfs that I have just created gives me the number of touristic residences per provincia

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


provincie = [
    'BELLUNO',
    'PADOVA',
    'TREVISO',
    'ROVIGO',
    'VENEZIA',
    'VERONA',
    'VICENZA'
]

city = st.selectbox("What Provincia do you want to analyze?", provincie)

fig = plt.figure(figsize=(30,10))

if city == 'BELLUNO':
    st.title('Informations of TR in Belluno')
    st.bar_chart(belluno_descriptive)
    st.text('Total',city_len[0], str(city_len[0]), ha='center', weight='bold')

elif city == 'PADOVA':
    fig.suptitle('Informations of TR in Padova', fontsize= 20)
    plt.bar('Total', city_len[1])
    plt.text('Total',city_len[1], str(city_len[1]), ha='center', weight='bold')
    for i in range(len(padova_descriptive)):
      plt.bar(padova_descriptive.index[i], padova_descriptive[i])
      plt.xticks(rotation=45)
      number = round((padova_descriptive[i]/padova_tr)*100,1)
      plt.text(padova_descriptive.index[i], padova_descriptive[i], str(number)+'%', ha='center', weight='bold')
    st.bar_chart(fig)

elif city == 'TREVISO':
    st.title('Informations of TR in Treviso')
    st.bar_chart(treviso_descriptive)
    st.text('Total',city_len[2], str(city_len[2]), ha='center', weight='bold')

elif city == 'ROVIGO':
    st.title('Informations of TR in Rovigo')
    st.bar_chart(rovigo_descriptive)
    st.text('Total',city_len[3], str(city_len[3]), ha='center', weight='bold')

elif city == 'VENEZIA':
    st.title('Informations of TR in Venezia')
    st.bar_chart(venezia_descriptive)
    st.text('Total',city_len[4], str(city_len[4]), ha='center', weight='bold')

elif city == 'VERONA':
    st.title('Informations of TR in Verona')
    st.bar_chart(verona_descriptive)
    st.text('Total',city_len[5], str(city_len[5]), ha='center', weight='bold')

elif city == 'VICENZA':
    st.title('Informations of TR in Vicenza')
    st.bar_chart(vicenza_descriptive)
    st.text('Total',city_len[6], str(city_len[6]), ha='center', weight='bold')




