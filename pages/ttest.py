import streamlit as st
import numpy as np
from scipy import stats

# Tampilkan judul aplikasi
st.title("Uji t (t-test)")

# Input data
group1 = st.text_area("Data kelompok 1 (pisahkan dengan koma)", "1, 2, 3, 4, 5")
group2 = st.text_area("Data kelompok 2 (pisahkan dengan koma)", "6, 7, 8, 9, 10")

# Mengubah input menjadi array numerik
group1 = np.fromstring(group1, sep=',')
group2 = np.fromstring(group2, sep=',')

# Hitung statistik uji t
t_statistic, p_value = stats.ttest_ind(group1, group2)

# Tampilkan hasil uji t
st.write("Hasil Uji t:")
st.write("T-Statistic:", t_statistic)
st.write("P-Value:", p_value)

# Berikan kesimpulan berdasarkan p-value
if p_value < 0.05:
    st.write("Kesimpulan: Terdapat perbedaan yang signifikan antara dua kelompok")
else:
    st.write("Kesimpulan: Tidak terdapat perbedaan yang signifikan antara dua kelompok")
