# pages/1_Materi_Klasifikasi.py
import streamlit as st
import os
from PIL import Image
import base64

# ==========================================================
# 🌸 1. KONFIGURASI DASAR & BACKGROUND PINK DREAMY
# ==========================================================
st.set_page_config(page_title="🌷 Materi Klasifikasi Gambar", layout="wide")

# ✅ Fungsi background agar sama dengan halaman utama
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

    /* Sidebar sama seperti halaman utama */
    [data-testid="stSidebar"] {{
        background: rgba(255, 240, 245, 0.9);
        backdrop-filter: blur(6px);
        border-right: 2px dashed #ffb6c1;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ==========================================================
# 🌺 2. GAYA TEMA (SAMA DENGAN HALAMAN UTAMA)
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Pacifico&display=swap');

/* 🌸 Semua font default pakai Poppins */
html, body, .stApp, div, p, span, label, input, button, select, textarea, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
    color: #000000;
}

/* 💖 Judul besar pakai Pacifico */
h1 {
    text-align: center;
    color: #ff66b2;
    font-family: 'Pacifico', cursive !important;
    font-size: 42px;
    text-shadow: 0 0 12px #ffd1dc, 0 0 20px #ffb6c1;
    margin-bottom: 10px;
}

/* 🌸 Card konten */
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

/* Animasi muncul lembut */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe6f2, #ffd6e8);
    border-right: 3px dashed #ffb6c1;
    box-shadow: 4px 0px 10px rgba(255,182,193,0.5);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
    color: #ff69b4 !important;
}

/* Audio Player */
audio {
    width: 70%;
    border-radius: 25px;
    background: #ffe6f0;
    box-shadow: 0 0 10px rgba(255,182,193,0.7);
    margin: 10px auto;
    display: block;
}

/* 🌸 Animasi bunga jatuh */
@keyframes float {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
.flower {
    position: fixed;
    top: -10vh;
    font-size: 24px;
    animation: float 10s linear infinite;
    z-index: 0;
}
.flower:nth-child(2) { left: 10%; animation-delay: 1s; }
.flower:nth-child(3) { left: 25%; animation-delay: 3s; }
.flower:nth-child(4) { left: 50%; animation-delay: 5s; }
.flower:nth-child(5) { left: 75%; animation-delay: 2s; }
.flower:nth-child(6) { left: 90%; animation-delay: 4s; }

</style>

<!-- 🌸 Ornamen bunga jatuh -->
<div class="flower">🌸</div>
<div class="flower">💖</div>
<div class="flower">🌺</div>
<div class="flower">💞</div>
<div class="flower">🌷</div>
<div class="flower">💕</div>
""", unsafe_allow_html=True)

# ==========================================================
# 🌷 3. JUDUL
# ==========================================================
st.markdown("<h1>🌷 Materi: Klasifikasi Gambar 🌷</h1>", unsafe_allow_html=True)

# ==========================================================
# 🎵 4. MUSIK (Cupid - Fifty Fifty)
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
# 🌼 5. CARD 1 — ISI MATERI
# ==========================================================
st.markdown("""
<div class='box'>
Klasifikasi gambar merupakan salah satu cabang penting dari <b>Computer Vision</b> yang berfungsi untuk mengenali dan mengelompokkan objek berdasarkan karakteristik visual dari sebuah gambar.  
Dalam penelitian atau sistem ini, model AI dirancang untuk melakukan <b>klasifikasi ke dalam delapan kelas utama</b>, yaitu:

1️⃣ Airplane — Model mengenali bentuk pesawat dari berbagai sudut pandang, termasuk sayap, ekor, dan badan pesawat. Objek ini umumnya memiliki warna metalik atau putih dengan bentuk aerodinamis.  
2️⃣ Car — Sistem mampu mendeteksi berbagai jenis mobil (sedan, SUV, truk kecil) berdasarkan struktur bodi, roda, dan jendela.  
3️⃣ Cat — Kelas ini berfokus pada ciri khas wajah dan postur tubuh kucing seperti telinga runcing, mata besar, dan bulu halus.  
4️⃣ Dog — Model membedakan anjing dari hewan lain dengan mengenali moncong, telinga, dan bentuk tubuhnya yang beragam antar ras.  
5️⃣ Flower — Mengidentifikasi bunga melalui bentuk kelopak, warna dominan, serta pola simetris alami yang khas.  
6️⃣ Fruit — Model mempelajari perbedaan tekstur dan warna pada berbagai buah seperti apel, jeruk, atau pisang.  
7️⃣ Motorbike — Fokus pada struktur kendaraan roda dua seperti roda, rangka, dan lampu depan.  
8️⃣ Person — Mendeteksi manusia dalam berbagai pose dan pakaian, baik seluruh tubuh maupun sebagian.

Model ini dibangun menggunakan <b>Convolutional Neural Network (CNN)</b> yang mampu mengekstraksi fitur visual secara otomatis dari data latih. CNN bekerja dengan lapisan konvolusi yang mendeteksi pola seperti tepi, sudut, hingga tekstur.  
Setelah melalui proses pelatihan dengan ribuan citra, model mampu mengenali pola visual dan melakukan prediksi dengan akurasi tinggi.

Dalam implementasinya, sistem ini dapat digunakan untuk berbagai kebutuhan seperti:

🔹 Sistem keamanan berbasis pengenalan objek (contoh: mendeteksi manusia atau kendaraan)  
🔹 Aplikasi katalog digital (contoh: mengelompokkan gambar produk berdasarkan kategori)  
🔹 Pembelajaran mesin pada bidang robotika dan otomasi penglihatan mesin  

Secara umum, tujuan utama klasifikasi 8 kelas ini adalah agar sistem dapat memahami konteks visual dari suatu gambar dan menempatkannya ke dalam kategori yang paling sesuai berdasarkan hasil analisis model.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# 🖼 6. CARD 2 — HANYA UNTUK JUDUL + STYLE CAPTION HITAM
# ==========================================================
image_folder = os.path.join(os.path.dirname(__file__), "../sample_images")

# Tambahkan CSS card2 agar konsisten
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

/* 🖤 Caption gambar biar benar-benar hitam dan tebal */
figure > figcaption, div[data-testid="stImage"] figcaption, .stImage figcaption {
    color: #000000 !important;
    font-weight: 700 !important;
    text-align: center !important;
    font-size: 14px !important;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
}
</style>
""", unsafe_allow_html=True)

# Card kedua hanya judul
st.markdown("<div class='card2'><h3>🖼 Contoh Gambar Klasifikasi 8 Kelas</h3></div>", unsafe_allow_html=True)

# ==========================================================
# 🖼 Gambar ditampilkan di luar card (caption hitam manual)
# ==========================================================
if os.path.exists(image_folder):
    images = [f for f in os.listdir(image_folder) if "klasifikasi" in f.lower()]
    cols = st.columns(4)
    for i, img_file in enumerate(sorted(images)):
        img_path = os.path.join(image_folder, img_file)
        with cols[i % 4]:
            st.image(Image.open(img_path), use_column_width=True)
            st.markdown(
                f"<p style='text-align:center; color:#000000; font-weight:600; font-size:14px;'>{img_file}</p>",
                unsafe_allow_html=True
            )
else:
    st.warning("Folder sample_images tidak ditemukan 😢")
    
# ==========================================================
# 🌸 7. CARD 3 — FOOTER DALAM CARD
# ==========================================================
st.markdown("""
<style>
.card3 {
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
}
</style>

<div class='card3'>
🌷 🌸 💖 🌺 💕 🌼 💗 🌹 🌻
</div>
""", unsafe_allow_html=True)

# ==========================================================
# 🌈 8. BACKGROUND DIPANGGIL TERAKHIR
# ==========================================================
add_bg_from_local("assets/background.jpg")