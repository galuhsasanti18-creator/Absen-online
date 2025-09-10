import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Absensi Kelas X2", layout="wide")

st.title("📋 Absensi Kelas X2 - SMAN 9 Bogor")
st.write("Wali Kelas: **Ibu Sri Lestari Setyaningsih**")

st.subheader("Form Absensi")

nama = st.text_input("✍️ Nama Lengkap")
status = st.radio(
    "Pilih Status Kehadiran",
    ["Belum Absen", "Hadir", "Izin", "Sakit", "Alfa"],
    index=0,
    horizontal=True
)
foto = st.camera_input("📸 Ambil Foto Kehadiran")

# Tombol simpan
if st.button("✅ Simpan Absensi"):
    if not nama:
        st.warning("Harap isi nama dulu!")
    else:
        st.session_state.setdefault("rekap", [])
        st.session_state["rekap"].append({
            "nama": nama,
            "status": status,
            "foto": foto
        })
        st.success(f"Absensi {nama} berhasil disimpan!")

# Rekap Kehadiran
st.subheader("📊 Rekap Kehadiran")
if "rekap" in st.session_state and st.session_state["rekap"]:
    for data in st.session_state["rekap"]:
        st.write(f"- {data['nama']}: **{data['status']}**")
        if data["foto"] is not None:
            st.image(data["foto"], width=120)

    # Convert ke DataFrame
    df = pd.DataFrame([
        {"Nama": d["nama"], "Status": d["status"]}
        for d in st.session_state["rekap"]
    ])

    # Simpan ke Excel di memory
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Absensi")
    buffer.seek(0)

    st.download_button(
        label="📥 Download Rekap Absensi (Excel)",
        data=buffer,
        file_name="rekap_absensi.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info("Belum ada data absensi yang masuk.")
