import streamlit as st
from PIL import Image
import numpy as np
import torch
from tensorflow.keras.models import load_model
from ultralytics import YOLO
import matplotlib.pyplot as plt
import base64

# ==========================================================
# 🌸 1. KONFIGURASI DASAR
# ==========================================================
st.set_page_config(page_title="💞 Anggiya Mahara | Dashboard Klasifikasi & Deteksi Gambar 💞", layout="wide")

# ==========================================================
# ✅ BACKGROUND IMAGE DENGAN OVERLAY PINK
# ==========================================================
def add_bg_from_local(image_file):
    """Tambahkan background dreamy pink lembut."""
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

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: rgba(255, 240, 245, 0.9);
        backdrop-filter: blur(6px);
        border-right: 2px dashed #ffb6c1;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ==========================================================
# 💗 2. TEMA & GAYA GLOBAL
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Pacifico&display=swap');

/* 🌸 Semua teks default (selain judul besar) pakai Poppins */
html, body, .stApp, div, p, span, label, input, button, select, textarea, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
}


/* 🌸 Wadah besar untuk seluruh konten utama */
.block-container {
    background: rgba(255, 255, 255, 0.50);  /* ⚪ Lebih transparan */
    border-radius: 25px;
    padding: 70px 40px;
    margin: 40px auto;
    max-width: 1000px;  /* 🌷 Membatasi lebar card */
    box-shadow: 0 8px 25px rgba(255,182,193,0.35);
    backdrop-filter: blur(4px);
}

/* Judul besar */
h1 {
    text-align: center;
    color: #ff66b2;
    font-family: 'Pacifico', cursive;
    font-size: 42px;
    text-shadow: 0 0 12px #ffd1dc, 0 0 20px #ffb6c1;
    margin-bottom: 10px;
}

/* Subtitle */
h3 {
    color: #d63384;
    font-weight: 700;
    text-shadow: 0px 0px 6px #ffb6c1;
}

/* Tombol utama */
div.stButton > button {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(90deg, #ffb6c1, #ff69b4);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 0.7em 1.4em;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(255,182,193,0.6);
}
div.stButton > button:hover {
    transform: scale(1.07);
    background: linear-gradient(90deg, #ff69b4, #ffa6c9);
    box-shadow: 0 0 18px #ff69b4;
}

/* Musik player */
audio {
    width: 70%;
    border-radius: 25px;
    background: #ffe6f0;
    box-shadow: 0 0 10px rgba(255,182,193,0.7);
    margin: 10px auto;
    display: block;
}

/* Animasi bunga jatuh */
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

/* Footer */
footer {
    text-align: center;
    color: #d63384;
    font-size: 20px;
    padding: 10px;
}
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
# 🌷 3. JUDUL & DESKRIPSI
# ==========================================================
st.markdown("<h1>💗 Dashboard Klasifikasi & Deteksi Gambar 💗</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Unggah gambar, pilih model, lalu lihat hasil prediksi AI dengan tampilan lembut dan manis penuh bunga 🌸💖</p>",
    unsafe_allow_html=True
)

# ==========================================================
# 🌼 4. SIDEBAR
# ==========================================================
st.sidebar.header("🧠 Pilih Model")
model_choice = st.sidebar.selectbox(
    "Model yang ingin digunakan:",
    ["Klasifikasi 8 kelas", "Deteksi Gender"]
)

# ==========================================================
# 🎵 5. MUSIK LATAR
# ==========================================================
st.markdown("""
<div style="
    text-align:center;
    background: rgba(255, 240, 245, 0.9);
    border: 2px solid #ffb6c1;
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 15px;
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
# 🌺 6. UPLOAD GAMBAR
# ==========================================================
uploaded_file = st.file_uploader("📤 Unggah gambar (JPG/PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Gambar yang diunggah", use_container_width=True)

# ==========================================================
# 🌹 7. LOAD MODEL
# ==========================================================
@st.cache_resource
def load_keras_model():
    return load_model("model/klasifikasi 8 kelas.h5")

@st.cache_resource
def load_torch_model():
    return YOLO("model/deteksi gender.pt")

# ==========================================================
# 🌻 8. PREDIKSI
# ==========================================================
def predict_keras(image_input):
    model = load_keras_model()
    img_resized = image_input.resize((128, 128))
    img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)
    pred = model.predict(img_array)
    class_idx = np.argmax(pred)
    class_labels = [
        "Airplane", "Car", "Cat", "Dog", "Flower", "Fruit", "Motorbike", "Person"
    ]
    return class_labels[class_idx], pred[0]

def predict_torch(image_input):
    model = load_torch_model()
    results = model.predict(image_input, imgsz=224, conf=0.5, verbose=False)
    if results[0].boxes is not None and len(results[0].boxes) > 0:
        boxes = results[0].boxes
        cls_idx = int(boxes.cls[0].item())
        conf = float(boxes.conf[0].item())
        label = f"{results[0].names[cls_idx]} ({conf:.2f})"
        st.image(results[0].plot(), caption="🎯 Hasil Deteksi YOLO")
        return label, [conf]
    return "Tidak ada deteksi ditemukan", [0.0]

if uploaded_file:
    if st.button("💫 Jalankan Prediksi Sekarang"):
        with st.spinner("Model sedang bekerja keras dengan penuh cinta... 💕"):
            if model_choice == "Klasifikasi 8 kelas":
                label, prob = predict_keras(image)
            else:
                label, prob = predict_torch(image)
        st.success("✨ Prediksi Berhasil!")
        st.markdown(f"<h3 style='text-align:center;'>🧾 Label: <span style='color:#d63384;'>{label}</span></h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots()
        bars = ax.bar(range(len(prob)), prob, color="#ff69b4", edgecolor="#d63384")
        labels = [f"K{i+1}" for i in range(len(prob))]
        ax.set_xticks(range(len(prob)))
        ax.set_xticklabels(labels)
        ax.set_ylabel("Probabilitas")
        ax.set_title("Grafik Probabilitas")
        for bar, p in zip(bars, prob):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{p:.2f}",
                    ha='center', va='bottom', fontsize=10, color="#d63384")
        st.pyplot(fig)

# ==========================================================
# 🌼 9. PANDUAN
# ==========================================================
st.markdown("""
*📘 Panduan Penggunaan*
1. Pilih materi: Klasifikasi atau Deteksi.
2. Pilih model sesuai kebutuhan.
3. Unggah gambar (format JPG atau PNG).
4. Klik *Jalankan Prediksi Sekarang*.
5. Lihat hasil berupa label dan grafik probabilitas.

💡 Gunakan gambar kecil agar proses lebih cepat!
""")

# ==========================================================
# 🌺 10. PENUTUP
# ==========================================================
st.markdown("""
<div style='text-align: center; font-size: 22px; margin-top: 30px;'>
🌷 🌸 💖 🌺 💕 🌼 💗 🌹 🌻
</div>
""", unsafe_allow_html=True)

# ==========================================================
# ✅ BACKGROUND DIPANGGIL TERAKHIR
# ==========================================================
add_bg_from_local("assets/background.jpg")