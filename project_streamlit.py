import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

st.title('__NICOLO AVESANI VR490189 PROGRAMMING FINAL PROJECT 2022-2023__')
st.text('Im Nicolò Avesani, Data Science student in Verona.')
st.text('My project is focused on a dataset called ''Touristic Residences in Veneto.')
st.text('The dataset has 8504 rows and 45 columns, describing all the main characteristics of the touristic residences in Veneto (Italy),')
st.text('such as the presence of: private pool, restaurant, private parking spots, staff ready to speak in several languages.')
st.text('Structures are divided in 7 Districts, the so-called Provincie, which are: Belluno, Padova, Rovigo, Treviso, Venezia, Verona, Vicenza.')
st.text('The analysis of the geographical location of the residenes will help understanding some results.')
st.text('The aim of my project is to find out if there is a positive correlation between the main descriptive variables and the classification of the touristic residences.')