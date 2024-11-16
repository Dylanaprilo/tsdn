import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json

def show():
    # Judul halaman
    st.title("Fasilitas Kesehatan")
    st.write("Informasi distribusi fasilitas kesehatan berdasarkan provinsi.")

    # Load dataset
    df = pd.read_csv('data/fasilitas_kesehatan.csv')  # Pastikan path file ini benar
    geojson_path = 'data/indonesia-province.geojson'  # GeoJSON file untuk provinsi Indonesia

    # Filter untuk tipe fasilitas kesehatan
    selected_faskes = st.selectbox(
        "Pilih Tipe Fasilitas Kesehatan",
        ["Semua"] + list(df['TipeFaskes'].unique())
    )

    # Filter data berdasarkan tipe fasilitas kesehatan
    filtered_df = df if selected_faskes == "Semua" else df[df['TipeFaskes'] == selected_faskes]

    # Menghitung jumlah fasilitas kesehatan berdasarkan provinsi
    faskes_per_provinsi = filtered_df['Provinsi'].value_counts().reset_index()
    faskes_per_provinsi.columns = ['Provinsi', 'JumlahFaskes']

    # Load GeoJSON file
    with open(geojson_path, 'r') as f:
        geojson_data = json.load(f)

    # Peta Distribusi Fasilitas Kesehatan
    st.write("### Peta Distribusi Fasilitas Kesehatan")
    m = folium.Map(location=[-2.5489, 118.0149], zoom_start=5)

    # Choropleth map
    choropleth = folium.Choropleth(
        geo_data=geojson_data,
        name="choropleth",
        data=faskes_per_provinsi,
        columns=["Provinsi", "JumlahFaskes"],
        key_on="feature.properties.state",  # Pastikan key GeoJSON sesuai dengan nama provinsi di dataset
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Jumlah Fasilitas Kesehatan"
    ).add_to(m)

    # Tooltip untuk informasi tambahan
    folium.LayerControl().add_to(m)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["name"], labels=False)
    )

    # Menampilkan peta di Streamlit
    st_folium(m, width=800, height=500)

    # Menampilkan tabel jumlah fasilitas kesehatan
    st.write("### Detail Jumlah Fasilitas Kesehatan per Provinsi")
    st.dataframe(faskes_per_provinsi)

    # Tombol Unduh Data
    csv = faskes_per_provinsi.to_csv(index=False)
    st.download_button(
        label="Download Data Fasilitas Kesehatan (CSV)",
        data=csv,
        file_name="fasilitas_kesehatan_per_provinsi.csv",
        mime="text/csv"
    )