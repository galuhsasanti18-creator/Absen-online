import streamlit as st

st.set_page_config(page_title="Absensi Kelas X2", layout="wide")

st.title("📋 Absensi Kelas X2 - SMAN 4 Madiun")
st.write("Wali Kelas: **Ibu Sri Lestari Setyaningsih**")

siswa = [
    "AGISTA DWI HERYANI", "AIRA SEKAR GALUH", "AKHDAN ZAINNAFI HIDAYAT",
    "ALEA RAHMA ADELIA", "ALI HADI ABDULLAH AL KHAZAL", "AMELIA ZAHRA AZATIL ISMAH",
    "ANINDYTA NABILA PUTRI", "ARFA AHMAD RASULA", "CHERYL FAREN", "DARWIN MAULANA",
    "DEA RAHMA FEBRIANI", "DELVIA SASKIA SUGIARTO", "FADLAN MALAIKA OKTAVIAN",
    "GENDIS SUMARTONO", "GERALDLANDRIANO GULTOM"
]

rekap = {}

st.subheader("Absensi Harian")

for nama in siswa:
    status = st.radio(
        f"{nama}",
        ["Belum Absen", "Hadir", "Izin", "Sakit", "Alfa"],
        index=0,
        horizontal=True,
        key=nama
    )
    rekap[nama] = status

st.subheader("📊 Rekap Kehadiran")
for nama, status in rekap.items():
    st.write(f"- {nama}: **{status}**")
