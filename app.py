import streamlit as st
from streamlit_option_menu import option_menu
from pages import sebaran_penyakit, fasilitas_kesehatan, panduan_penanganan, laporan_penyakit, profile

import streamlit as st

st.set_page_config(
    page_title="Sebaran Penyakit Menular",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",  # Sidebar default tertutup
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None,
    }
)

# CSS untuk menyembunyikan ikon Streamlit dan header sidebar
st.markdown(
    """
    <style>
    /* Hides the Streamlit header and footer */
    header, .css-1d391kg { 
        visibility: hidden;
    }
    /* Custom sidebar styling */
    .css-18e3th9 {
        padding: 10px;
    }
    .sidebar .sidebar-content {
        width: 250px;
        padding: 10px;
        background-color: #23272a;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menyusun sidebar menggunakan `option_menu`
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Sebaran Penyakit Menular", "Fasilitas Kesehatan", "Panduan Penanganan Penyakit", 
         "Laporan Penyakit Menular", "Profile"],
        icons=["map", "hospital", "book", "clipboard-data", "person"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px 0", "background-color": "#23272a"},
            "icon": {"color": "#ffffff", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#5865f2",
            },
            "nav-link-selected": {"background-color": "#5865f2"},
        },
    )

# Menampilkan halaman berdasarkan pilihan menu
if selected == "Sebaran Penyakit Menular":
    sebaran_penyakit.show()
elif selected == "Fasilitas Kesehatan":
    fasilitas_kesehatan.show()
elif selected == "Panduan Penanganan Penyakit":
    panduan_penanganan.show()
elif selected == "Laporan Penyakit Menular":
    laporan_penyakit.show()
elif selected == "Profile":
    profile.show()
