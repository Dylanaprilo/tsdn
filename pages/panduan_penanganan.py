import streamlit as st
import requests

# API key dari NewsAPI
API_KEY = "38aa7a53161a443e8cc50eff35a47d96"
BASE_URL = "https://newsapi.org/v2/everything"

def get_news(keyword, language="id", page_size=5):
    """
    Mengambil berita terkini berdasarkan keyword.
    
    Args:
    - keyword (str): Kata kunci pencarian berita.
    - language (str): Bahasa berita (default: 'id' untuk Indonesia).
    - page_size (int): Jumlah berita yang diambil per halaman.
    
    Returns:
    - list: Daftar berita yang ditemukan.
    """
    params = {
        "q": keyword,
        "apiKey": API_KEY,
        "language": language,
        "pageSize": page_size
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return []

def show():
    st.title("Panduan Penanganan Penyakit")
    st.write("Berikut adalah panduan utama dari Kementerian Kesehatan untuk penanganan penyakit menular.")
    st.image("panduan.png", width=400)
    st.markdown("[Baca Selengkapnya](https://rc.kemkes.go.id/unduh-booklet-dan-panduan-dd7f3a)")

    st.subheader("Artikel Kesehatan")
    
    # Tampilkan berita terkini
    st.subheader("Berita Terkini tentang Penyakit Menular")
    berita = get_news("Penyakit menular", page_size=5)
    
    if berita:
        for i, item in enumerate(berita, start=1):
            # Menampilkan judul
            st.markdown(f"### {i}. {item['title']}")
            
            # Menampilkan gambar jika ada
            if item.get('urlToImage'):
                st.image(item['urlToImage'], width=400)
            
            # Menampilkan sumber dan link
            st.markdown(f"**Sumber**: {item['source']['name']}")
            st.markdown(f"[Baca Selengkapnya]({item['url']})")
            st.markdown("---")
    else:
        st.warning("Tidak ada berita yang ditemukan.")

# Jalankan fungsi utama jika ini file utama
if __name__ == "__main__":
    show()
