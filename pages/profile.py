import streamlit as st

def show():
    st.title("Profile")
    st.write("Informasi Profile Pengguna")

    with st.form("profile_form"):
        full_name = st.text_input("Full Name")
        nickname = st.text_input("Nick Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        country = st.text_input("Country")
        language = st.selectbox("Language", ["English", "Indonesian", "Other"])
        timezone = st.text_input("Time Zone")

        submitted = st.form_submit_button("Save")
        if submitted:
            st.success("Profile saved successfully!")
