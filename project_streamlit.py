import streamlit as st
import pandas as pd


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




