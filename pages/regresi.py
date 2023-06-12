import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Tampilkan judul aplikasi
st.title("Regresi Linier Sederhana")

# Input data
st.write("Masukkan data:")
n = st.number_input("Jumlah data", min_value=2, step=1)
data = []
for i in range(n):
    x = st.number_input(f"Nilai X{i+1}")
    y = st.number_input(f"Nilai Y{i+1}")
    data.append((x, y))

# Konversi data menjadi dataframe
df = pd.DataFrame(data, columns=["X", "Y"])

# Tampilkan data
st.write("Data:")
st.write(df)

# Pilih kolom sebagai variabel independen (X) dan variabel dependen (Y)
x_column = st.selectbox("Pilih kolom sebagai variabel independen (X)", df.columns)
y_column = st.selectbox("Pilih kolom sebagai variabel dependen (Y)", df.columns)

# Split data menjadi X dan Y
X = df[x_column].values.reshape(-1, 1)
Y = df[y_column].values

# Fit regresi linier sederhana
model = LinearRegression()
model.fit(X, Y)

# Prediksi Y berdasarkan X
Y_pred = model.predict(X)

# Hitung koefisien korelasi
correlation = np.corrcoef(X.ravel(), Y)[0, 1]

# Tampilkan hasil regresi linier sederhana dan koefisien korelasi
st.write("Hasil Regresi Linier Sederhana:")
st.write("Koefisien Regresi (Intercept):", model.intercept_)
st.write("Koefisien Regresi (Slope):", model.coef_[0])
st.write("Koefisien Korelasi:", correlation)

# Plot data dan garis regresi
fig, ax = plt.subplots()
ax.scatter(X, Y, color='b', label='Data')
ax.plot(X, Y_pred, color='r', label='Regresi Linier')
ax.set_xlabel(x_column)
ax.set_ylabel(y_column)
ax.legend()

# Tampilkan grafik
st.pyplot(fig)
