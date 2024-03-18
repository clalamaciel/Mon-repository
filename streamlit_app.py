import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSkifjjijhyCfiL_eySZW_xKo_ltheX-uvNH4IsK2DjuCPeQdqJqYAoLiJX0HVKFJUAImN1M8cRhl_N/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Pinyin'].values[i]
st.write(word_fr+"Hanzi"+word_chi)
st.button("refresh")
