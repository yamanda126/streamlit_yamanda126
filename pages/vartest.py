import streamlit as st
import numpy as np
from scipy import stats

# Tampilkan judul aplikasi
st.title("Uji Hipotesis Varians Dua Populasi")

# Input data
data1 = st.text_area("Data Populasi 1 (pisahkan dengan koma dan spasi)", "1, 2, 3, 4, 5")
data2 = st.text_area("Data Populasi 2 (pisahkan dengan koma dan spasi)", "2, 4, 6, 8, 10")

# Mengubah input menjadi array numerik
data1 = np.fromstring(data1, sep=', ')
data2 = np.fromstring(data2, sep=', ')

# Hitung statistik uji
var1 = np.var(data1, ddof=1)
var2 = np.var(data2, ddof=1)
n1 = len(data1)
n2 = len(data2)
test_statistic = var1 / var2

# Hitung p-value dengan menggunakan distribusi F
p_value = stats.f.cdf(test_statistic, n1 - 1, n2 - 1)

# Tampilkan hasil uji
st.write("Hasil Uji Hipotesis:")
st.write("Varians Populasi 1:", var1)
st.write("Varians Populasi 2:", var2)
st.write("Uji Statistik:", test_statistic)
st.write("P-Value:", p_value)

# Berikan kesimpulan berdasarkan p-value
alpha = 0.05  # Tingkat signifikansi
if p_value < alpha:
    st.write("Kesimpulan: Terdapat perbedaan yang signifikan antara varians dua populasi")
else:
    st.write("Kesimpulan: Tidak terdapat perbedaan yang signifikan antara varians dua populasi")
