import streamlit as st
from PIL import Image

st.subheader("Aplikasi Sederhana")
st.text("Muhammad Sultan Al Faritz")
st.title("Kalkulator Tinggi Potensi Genetik")
st.image("tinggi badan.webp",width=600)
st.text("")
st.text("""Ini adalah program untuk menghitung range(minimum dan maksimum) tinggi badan anda.
--------------------------------------------------------------------------------------------
Tinggi badan seseorang tidak terlepas dari faktor genetik. Terkadang seseorang 
menginginkan tinggi badan yang lebih. padahal, beliau sudah berada pada tinggi
badan maksimum. Sebaliknya, terkadang seseorang menganggap bahwa dirinya sudah 
berada pada tinggi badan maksimum. Padahal, tinggi badannya masih jauh dibawah
tinggi maksimum dirinya, yang artinya masih memiliki potensi untuk mencapai 
tinggi badan maksimum. Dan tentunya untuk menambah tinggi badan, anda harus
berada dalam masa pertumbuhan. Berikut kalkulator tinggi potensi genetik.
--------------------------------------------------------------------------------------------""")
def input_tb():
    global tb_ayah
    global tb_ibu
    tb_ayah = st.number_input("Masukkan tinggi badan ayah (cm)",0)
    tb_ibu = st.number_input("Masukkan tinggi badan ibu (cm)",0)
def hitung_tb():
    tb_min = tb - 8.5
    tb_max = tb + 8.5
    hitung = st.button("hitung")
    if hitung:
        st.success("Range tinggi badan kamu : ")
        st.success(f"Minimum  = {tb_min}cm")
        st.success(f"Maksimum = {tb_max}cm")
        st.balloons()

jenis_kelamin = st.selectbox("",["Pilih jenis kelamin","Laki-laki","Perempuan"])
if jenis_kelamin == "Laki-laki":
    input_tb()
    tb = ((tb_ibu + 13 + tb_ayah) / 2)
    hitung_tb()
elif jenis_kelamin == "Perempuan":
    input_tb()
    tb = ((tb_ayah - 13 + tb_ibu) / 2)
    hitung_tb()
