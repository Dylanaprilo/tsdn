import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    # Judul halaman
    st.title("Laporan Penyakit Menular")
    st.write("Laporan akumulasi jumlah kasus penyakit menular berdasarkan provinsi dan jenis penyakit.")

    # Load dataset
    df = pd.read_csv('data/cleaned_dataset.csv')  # Pastikan path file ini benar

    # Konversi kolom 'Tanggal' ke format datetime jika diperlukan
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')

    # Membuat pivot table untuk mengakumulasi jumlah kasus per provinsi dan penyakit
    laporan_tabel = df.pivot_table(
        index='Provinsi',
        columns='Jenis Penyakit',
        values='Jumlah Kasus',
        aggfunc='sum',
        fill_value=0
    ).reset_index()

    # Menampilkan tabel hasil akumulasi
    st.write("### Tabel Laporan Akumulasi Kasus per Provinsi")
    st.dataframe(laporan_tabel)

    # Download laporan sebagai file CSV
    csv = laporan_tabel.to_csv(index=False)
    st.download_button(
        label="Download Laporan CSV",
        data=csv,
        file_name="laporan_penyakit_akumulasi.csv",
        mime="text/csv"
    )

    # Menampilkan Chart
    st.write("### Grafik Laporan")
    provinsi = st.selectbox("Pilih Provinsi untuk Grafik", laporan_tabel['Provinsi'])

    if provinsi:
        # Filter data untuk provinsi yang dipilih
        provinsi_data = laporan_tabel[laporan_tabel['Provinsi'] == provinsi].iloc[:, 1:]
        
        # Membuat bar chart
        plt.figure(figsize=(10, 6))
        provinsi_data.T.plot(kind='bar', legend=False, color='skyblue')
        plt.title(f"Jumlah Kasus di Provinsi {provinsi}", fontsize=16)
        plt.xlabel("Jenis Penyakit")
        plt.ylabel("Jumlah Kasus")
        plt.xticks(rotation=45, fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)
