import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest
import math

st.title("ztest")

df = pd.read_csv("https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv")

with st.expander("view data"):
    st.dataframe(df.transpose())

with st.expander("view statistics"):
    st.dataframe(df.describe().transpose())

st.write('## Constructing Hypothesis')

alpha = 0.05
alpha_z = NormalDist().inv_cdf(p=1-alpha/2)

null_mean = 67.5
z_score, p_value = ztest(df['grades'], value=null_mean, alternative= 'two-sided')

clicked = st.button('DO the Z test!!')

if clicked:
    if abs(z_score)>alpha_z:
        st.write('reject H0')
    else:
        st.write('can not reject H0')

    st.write(z_score, alpha_z)