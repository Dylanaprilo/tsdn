import pandas as pd

# Path ke file dataset
input_path = r'C:\Users\Dylan\Downloads\datapenyekitinfeksiuskotalokal(REAL).csv'
output_path = r'C:\Users\Dylan\Downloads\cleaned_dataset.csv'

# Membaca dataset
df = pd.read_csv(input_path)

# Filter untuk kolom jenis penyakit
allowed_diseases = [
    "Dengue", "Gonorrhea", "Hepatitis B, Acute", 
    "HIV", "Influenza Death (<65 years of age)", 
    "Malaria", "Tuberculosis"
]
df = df[df['Jenis Penyakit'].isin(allowed_diseases)]

# Hapus baris dengan jumlah kasus (Count) bernilai 0
df = df[df['Jumlah Kasus'] > 0]

# Filter data untuk kolom tahun (year)
allowed_years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')  # Konversi ke datetime
df = df[df['Tanggal'].dt.year.isin(allowed_years)]

# Simpan dataset yang sudah dibersihkan ke file baru
df.to_csv(output_path, index=False)
print(f"Data berhasil dicleaning dan disimpan sebagai '{output_path}'")
