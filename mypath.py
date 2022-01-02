import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title ("Streamlit 超入門")

st.write('Display Image')

if st.checkbox('Show Image'):
   img = Image.open('zonbigakki-.jpeg')
   st.image(img, caption='Gakki-', use_column_width=True)

#
# st.table(df.style.highlight_max(axis=0))

