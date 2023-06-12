import streamlit as st
import numpy as np
from scipy import stats

# Tampilkan judul aplikasi
st.title("Uji ANOVA")

# Input data
group1 = st.text_area("Data Kelompok 1 (pisahkan dengan koma dan spasi)", "1, 2, 3, 4, 5")
group2 = st.text_area("Data Kelompok 2 (pisahkan dengan koma dan spasi)", "2, 4, 6, 8, 10")
group3 = st.text_area("Data Kelompok 3 (pisahkan dengan koma dan spasi)", "3, 6, 9, 12, 15")

# Mengubah input menjadi array numerik
group1 = np.fromstring(group1, sep=', ')
group2 = np.fromstring(group2, sep=', ')
group3 = np.fromstring(group3, sep=', ')

# Hitung statistik uji
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

# Tampilkan hasil uji
st.write("Hasil Uji ANOVA:")
st.write("F-Statistic:", f_statistic)
st.write("P-Value:", p_value)

# Berikan kesimpulan berdasarkan p-value
alpha = 0.05  # Tingkat signifikansi
if p_value < alpha:
    st.write("Kesimpulan: Terdapat perbedaan yang signifikan antara setidaknya dua kelompok")
else:
    st.write("Kesimpulan: Tidak terdapat perbedaan yang signifikan antara kelompok-kelompok")

