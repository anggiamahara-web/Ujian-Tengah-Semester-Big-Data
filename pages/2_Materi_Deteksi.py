# pages/2_Materi_Deteksi.py
import streamlit as st
import os
from PIL import Image
import base64

# ==========================================================
# 🌸 1. KONFIGURASI DASAR & BACKGROUND PINK DREAMY
# ==========================================================
st.set_page_config(page_title="🌺 Materi Deteksi Objek", layout="wide")

def add_bg_from_local(image_file):
    """Tambahkan background dreamy pink lembut (konsisten dengan halaman utama)."""
    with open(image_file, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image:
            linear-gradient(rgba(255, 240, 246, 0.35), rgba(255, 200, 230, 0.35)),
            url("data:image/jpg;base64,{encoded_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stSidebar"] {{
        background: rgba(255, 240, 245, 0.9);
        backdrop-filter: blur(6px);
        border-right: 2px dashed #ffb6c1;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


# ==========================================================
# 🌺 2. GAYA TEMA (SAMA DENGAN HALAMAN KLASIFIKASI)
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Pacifico&display=swap');
html, body, .stApp, div, p, span, label, input, button, select, textarea, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
    color: #000000;
}

h1 {
    text-align: center;
    color: #ff66b2;
    font-family: 'Pacifico', cursive !important;
    font-size: 42px;
    text-shadow: 0 0 12px #ffd1dc, 0 0 20px #ffb6c1;
    margin-bottom: 10px;
}

.box {
    background: rgba(255, 255, 255, 0.50);
    border-radius: 25px;
    padding: 40px 50px;
    margin: 40px auto;
    max-width: 950px;
    box-shadow: 0 8px 25px rgba(255,182,193,0.35);
    backdrop-filter: blur(5px);
    animation: fadeIn 1s ease-out;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

audio {
    width: 70%;
    border-radius: 25px;
    background: #ffe6f0;
    box-shadow: 0 0 10px rgba(255,182,193,0.7);
    margin: 10px auto;
    display: block;
}

.flower {
    position: fixed;
    top: -10vh;
    font-size: 24px;
    animation: float 10s linear infinite;
    z-index: 0;
}
@keyframes float {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
</style>

<div class="flower">🌸</div>
<div class="flower">💖</div>
<div class="flower">🌺</div>
<div class="flower">💞</div>
<div class="flower">🌷</div>
<div class="flower">💕</div>
""", unsafe_allow_html=True)


# ==========================================================
# 🌷 3. JUDUL HALAMAN
# ==========================================================
st.markdown("<h1>🌺 Materi: Deteksi Objek 🌺</h1>", unsafe_allow_html=True)

# ==========================================================
# 🎵 4. MUSIK DI CARD PINK
# ==========================================================
st.markdown("""
<div style="
    text-align:center;
    background: rgba(255, 240, 245, 0.9);
    border: 2px solid #ffb6c1;
    border-radius: 20px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 4px 10px rgba(255,182,193,0.5);
    width: 80%;
    margin-left: auto;
    margin-right: auto;
">
    <p style="font-size:18px; color:#d63384; font-weight:600;">
        💞🎧 Lagi muter: <span style="color:#ff69b4;">Cupid - Fifty Fifty</span> 💕
    </p>
</div>
""", unsafe_allow_html=True)
st.audio("assets/Cupid.mp3", format="audio/mp3", start_time=0)

# ==========================================================
# 🌼 5. CARD 1 — ISI MATERI DETEKSI
# ==========================================================
st.markdown("""
<div class='box'>
Deteksi gender merupakan penerapan <b>Computer Vision</b> untuk mengenali dan membedakan jenis kelamin seseorang berdasarkan fitur visual pada wajah maupun tubuh.  
Pada sistem ini, model AI dirancang untuk mengidentifikasi dua kategori utama: <b>Men (Laki-laki)</b> dan <b>Women (Perempuan)</b>.

### 🧠 Prinsip Kerja Deteksi Gender
Model deteksi gender biasanya dilatih menggunakan ribuan citra wajah manusia dengan variasi ekspresi, usia, dan pencahayaan.  
Algoritma <b>YOLO (You Only Look Once)</b> digunakan karena kemampuannya melakukan deteksi secara cepat dan akurat dalam satu kali pemrosesan citra.

Langkah-langkah utamanya meliputi:

1️⃣ Preprocessing Gambar — Wajah dideteksi dan dipotong dari gambar asli.  
2️⃣ Ekstraksi Fitur Visual — Model menganalisis fitur khas seperti bentuk rahang, alis, panjang rambut, dan proporsi wajah.  
3️⃣ Klasifikasi — Berdasarkan fitur tersebut, model menentukan apakah objek tergolong "Men" atau "Women".  
4️⃣ Bounding Box Output — Model menampilkan hasil deteksi berupa kotak di sekitar wajah dengan label dan tingkat kepercayaan (confidence score).

### 💡 Aplikasi Deteksi Gender
- Sistem keamanan dan pengawasan berbasis kamera (mengetahui proporsi gender di area tertentu).  
- Analisis demografis dalam event atau pusat perbelanjaan.  
- Optimalisasi konten dan iklan berdasarkan kategori pengguna.  
- Pengembangan sistem interaksi manusia-komputer (seperti robot atau asisten digital).  

Deteksi gender bukan hanya sekadar mengenali wajah, tetapi juga memahami pola visual kompleks dari fitur wajah manusia.  
Dengan memanfaatkan teknologi YOLO, sistem ini mampu melakukan deteksi <b>real-time</b> dengan tingkat akurasi tinggi tanpa mengorbankan kecepatan inferensi.

Model ini tetap harus dilatih secara etis dan beragam, memastikan bahwa sistem tidak bias terhadap ras, usia, atau kondisi pencahayaan tertentu.
</div>
""", unsafe_allow_html=True)


# ==========================================================
# 🖼 6. CARD 2 — JUDUL + CONTOH GAMBAR DETEKSI
# ==========================================================
st.markdown("""
<style>
.card2 {
    background: rgba(255, 255, 255, 0.50);
    border-radius: 25px;
    padding: 10px 50px;
    margin: 40px auto 20px auto;
    max-width: 950px;
    box-shadow: 0 8px 25px rgba(255,182,193,0.35);
    backdrop-filter: blur(5px);
    animation: fadeIn 1s ease-out;
}
.card2 h3 {
    text-align: center;
    color: #000000;
    font-weight: 700;
    font-size: 22px;
    text-shadow: 0 0 8px #ffd1dc;
    margin: 0;
}

/* 🖤 Caption gambar */
figure > figcaption, div[data-testid="stImage"] figcaption, .stImage figcaption {
    color: #000000 !important;
    font-weight: 700 !important;
    text-align: center !important;
    font-size: 14px !important;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
}
</style>
<div class='card2'><h3>📸 Contoh Gambar Deteksi Gender</h3></div>
""", unsafe_allow_html=True)

image_folder = os.path.join(os.path.dirname(__file__), "../sample_images")
if os.path.exists(image_folder):
    images = [f for f in os.listdir(image_folder) if "deteksi" in f.lower()]
    cols = st.columns(3)
    for i, img_file in enumerate(sorted(images)):
        img_path = os.path.join(image_folder, img_file)
        with cols[i % 3]:
            st.image(Image.open(img_path), use_column_width=True)
            st.markdown(
                f"<p style='text-align:center; color:#000000; font-weight:600; font-size:14px;'>{img_file}</p>",
                unsafe_allow_html=True
            )
else:
    st.warning("Folder sample_images tidak ditemukan 😢")

# ==========================================================
# 🌸 7. CARD 3 — FOOTER
# ==========================================================
st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.50);
    border-radius: 25px;
    padding: 20px 50px;
    margin: 40px auto 20px auto;
    max-width: 950px;
    box-shadow: 0 8px 25px rgba(255,182,193,0.35);
    backdrop-filter: blur(5px);
    text-align: center;
    font-size: 22px;
    animation: fadeIn 1s ease-out;
">
🌷 🌸 💖 🌺 💕 🌼 💗 🌹 🌻
</div>
""", unsafe_allow_html=True)

# ==========================================================
# 🌈 8. BACKGROUND DIPANGGIL TERAKHIR
# ==========================================================
add_bg_from_local("assets/background.jpg")