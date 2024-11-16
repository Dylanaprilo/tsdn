import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def show():
    st.image("logo.jpg", width=400) 
    st.title("Sebaran Penyakit Menular")
    st.write("Informasi Data dan Visualisasi Penyebaran Penyakit Menular")

    # Load cleaned dataset
    df = pd.read_csv(r'data/cleaned_dataset.csv')  # Pastikan file ini ada di direktori yang benar

    # Konversi kolom 'Tanggal' ke datetime untuk memastikan data dalam format yang benar
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')

    # Filter untuk pilihan tahun dan jenis penyakit
    year = st.selectbox("Pilih Tahun", sorted(df['Tanggal'].dt.year.dropna().unique()))
    disease = st.selectbox("Nama Penyakit", df['Jenis Penyakit'].unique())

    # Filter dataset berdasarkan tahun dan jenis penyakit
    filtered_df = df[(df['Tanggal'].dt.year == year) & (df['Jenis Penyakit'] == disease)]

    # Menampilkan pengaturan filter lain
    st.write("### Filter Lain")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Media Penyebaran", ["Semua Media", "Makanan", "Udara", "Air", "Kontak Langsung"])
    with col2:
        selected_province = st.selectbox("Provinsi", ["Semua Provinsi"] + list(df['Provinsi'].unique()))
    with col3:
        st.selectbox("Gender", ["Semua Gender", "Laki-Laki", "Perempuan"])

    # Filter lebih lanjut jika provinsi tertentu dipilih
    if selected_province != "Semua Provinsi":
        filtered_df = filtered_df[filtered_df['Provinsi'] == selected_province]

    # Menampilkan Peta dengan warna representasi jumlah kasus
    m = folium.Map(location=[-2.5489, 118.0149], zoom_start=5)  # Pusat di Indonesia

    # Membuat Choropleth berdasarkan jumlah kasus
    folium.Choropleth(
        geo_data=r'data/indonesia-province.geojson',  # Path ke file GeoJSON untuk provinsi di Indonesia
        name="choropleth",
        data=filtered_df,
        columns=["Provinsi", "Jumlah Kasus"],
        key_on="feature.properties.state", 
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Jumlah Kasus"
    ).add_to(m)

    # Menambahkan marker untuk setiap lokasi dalam dataset
    for _, row in filtered_df.iterrows():
        latitude = row.get('latitude', -6.200000)  # Default latitude jika tidak tersedia
        longitude = row.get('longitude', 106.816666)  # Default longitude jika tidak tersedia
        folium.CircleMarker(
            location=(latitude, longitude),
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

    # Tampilkan peta
    st_folium(m, width=700, height=400)

    # Menampilkan tabel data
    st.write("### Detail Penyebaran Penyakit")
    st.write(filtered_df[['Tanggal', 'Jenis Penyakit', 'Provinsi', 'Jumlah Kasus']])