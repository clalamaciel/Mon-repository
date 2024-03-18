import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSkifjjijhyCfiL_eySZW_xKo_ltheX-uvNH4IsK2DjuCPeQdqJqYAoLiJX0HVKFJUAImN1M8cRhl_N/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_chi=voc['Hanzi'].values[i]
indices=np.random.choice(l,size=4,replace=false)
j=np.random.choice(indices)
word_fr=voc['Définition'].values[j]
st.write("Traduis:"+word.fr)
st.button("refresh")
