# pages/3_Tentang_Penulis.py
import streamlit as st
import base64
import os

st.set_page_config(page_title="🌷 Tentang Penulis dan Dashboard", layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255,240,246,0.35), rgba(255,200,230,0.35)),
            url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255,240,245,0.9);
        border-right: 2px dashed #ffb6c1;
        backdrop-filter: blur(6px);
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------- GAYA GLOBAL ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Pacifico&display=swap');
body, .stApp {font-family:'Poppins',sans-serif;color:#000}
h1{font-family:'Pacifico',cursive;color:#ff66b2;text-align:center;text-shadow:0 0 12px #ffd1dc;}
.box{
  background:rgba(255,255,255,0.55);
  border-radius:25px;
  box-shadow:0 8px 25px rgba(255,182,193,0.35);
  backdrop-filter:blur(6px);
  margin:40px auto;
  max-width:950px;
  padding:40px 50px;
}
.profile-img{
  width:260px;
  border-radius:25px;
  border:3px solid rgba(255,182,193,0.7);
  box-shadow:0 4px 12px rgba(255,182,193,0.4);
}
.caption{
  text-align:center;
  font-weight:600;
  color:#000000;
  margin-top:5px;
  font-size:14px;
}
.profile-flex{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  gap:40px;
  justify-content:center;
}
.profile-text{flex:1;min-width:280px}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🌷 Tentang Penulis dan Dashboard 🌷</h1>", unsafe_allow_html=True)

# ---------- CARD PROFIL ----------
img_path = "assets/Anggiya.jpg"
if not os.path.exists(img_path):
    st.warning("Tambahkan foto profil di: assets/Anggiya.jpg")

st.markdown(f"""
<div class="box">
  <div class="profile-flex">
    <div>
      <img src="data:image/jpg;base64,{base64.b64encode(open(img_path,"rb").read()).decode()}" class="profile-img">
      <div class="caption">Anggiya Mahara</div>
    </div>
    <div class="profile-text">
      <h3>💫 Biodata Singkat</h3>
      <p><b>Nama:</b> Anggiya Mahara<br>
      <b>NPM:</b> 2208108010083<br>
      <b>Jurusan:</b> Statistika<br>
      <b>Fakultas:</b> Matematika dan Ilmu Pengetahuan Alam — Universitas Syiah Kuala</p>
      <p>Mahasiswa yang mendalami pengembangan sistem berbasis <b>Artificial Intelligence</b> dan <b>Machine Learning</b>, dengan perhatian khusus pada pemanfaatan <b>Big Data</b> untuk menghasilkan analisis yang tepat dan bermanfaat.</p> 
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- CARD PROYEK ----------
st.markdown("""
<div class='box'>
<h3 style="text-align:center; color:#000000;">💻 Tentang Proyek Ini</h3>

Dashboard ini dikembangkan sebagai bagian dari pembelajaran dan riset mengenai 
<b>Computer Vision</b> dan <b>Deep Learning</b>.  
<br>
Proyek ini mengintegrasikan dua kemampuan utama:

1️⃣ <b>Klasifikasi Gambar</b> — Model AI mengenali 8 kelas objek (Airplane, Car, Cat, Dog, Flower, Fruit, Motorbike, Person).  
2️⃣ <b>Deteksi Gender</b> — Menggunakan arsitektur YOLO untuk mendeteksi dan membedakan manusia berdasarkan jenis kelamin.

Tujuan proyek ini adalah menghadirkan pengalaman belajar yang interaktif, menyenangkan, dan penuh sentuhan estetika dengan tema “Pink Kawaii Edition” 🌸💞.

Diharapkan dashboard ini dapat menjadi inspirasi bagi mahasiswa lain untuk memadukan sains data, AI, dan desain UI modern.
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="box" style="text-align:center;font-size:22px;">
🌷 🌸 💖 🌺 💕 🌼 💗 🌹 🌻  
<p style='font-size:14px;color:#000;'>© 2025 Anggiya Mahara | Dashboard Klasifikasi & Deteksi Gambar</p>
</div>
""", unsafe_allow_html=True)

add_bg_from_local("assets/background.jpg")