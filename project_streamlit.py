import streamlit as st
import pandas as pd


st.title('Touristic Residences in Veneto :lion_face:')
st.title('Nicolò Avesani VR490189, Final Project')

st.header('## 1 Explore and Clean the Dataset')

st.text('Firstly, I import the dataset using pandas. That is how it looks like:')

tourism_structures_df = pd.read_csv('https://www.veneto.eu/static/opendata/dove-alloggiare.csv')

st.dataframe(tourism_structures_df)

st.text('Information about the original dataset:')

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
st.text('As I can see, the dataset have 45 columns and 8504 rows.')
st.text('The data are for the majority composed by objects(43), with string values!')
st.text('Since I want to analyze the characteristics of the touristic residences,')
st.text('I need to trensform all the data with string values')
st.text('to boolean values 1 (True = Vero) and 0 (False = Falso)')

## Since the majority of data are string values, so I need to transform them into boolean values with 1 for True(Vero) and 0 for False (Falso)

for i in range(len(tourism_structures_df)):
  for j in tourism_structures_df.columns:
    if (tourism_structures_df[j][i] == 'Vero') | (tourism_structures_df[j][i] == 'Falso'):
      tourism_structures_df[j] = tourism_structures_df[j].map({'Vero':1,'Falso':0}) 

## i want to see the informations of the adjusted dataset

tourism_structures_df.info()

## as i can see, the dataset has a total of 8504 entries and 45 clolumns

