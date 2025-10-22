import streamlit as st
from PIL import Image
import numpy as np
import torch
from tensorflow.keras.models import load_model
from ultralytics import YOLO


# ==========================================================
# 🌸 1. KONFIGURASI DASAR
# ==========================================================
st.set_page_config(page_title="💞 AI Image Classifier — Kawaii Edition 💞", layout="wide")

# 💗 Tema super gemesh pink pastel dengan animasi bunga & love jatuh
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Pacifico&display=swap');

body, .stApp {
    background: linear-gradient(135deg, #fff0f6, #ffe4ec, #ffd6e8);
    font-family: 'Poppins', sans-serif;
    color: #4a4a4a;
    overflow-x: hidden;
}

/* ✨ Animasi bunga & love jatuh */
@keyframes float {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
.flower, .heart {
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

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe6f2, #ffd6e8);
    border-right: 3px dashed #ffb6c1;
    box-shadow: 4px 0px 10px rgba(255,182,193,0.5);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
    color: #ff69b4 !important;
}

/* Tombol utama */
div.stButton > button {
    background: linear-gradient(90deg, #ffb6c1, #ff69b4);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 0.7em 1.4em;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(255, 182, 193, 0.6);
}
div.stButton > button:hover {
    transform: scale(1.07);
    background: linear-gradient(90deg, #ff69b4, #ffa6c9);
    box-shadow: 0 0 18px #ff69b4;
}

/* Kotak hasil prediksi */
.result-box {
    background: rgba(255, 240, 245, 0.95);
    border-radius: 25px;
    border: 3px double #ffb6c1;
    padding: 25px;
    margin-top: 25px;
    box-shadow: 0 6px 15px rgba(255,182,193,0.4);
    animation: fadeIn 1s ease-out;
}

/* Animasi muncul lembut */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Audio player custom cute */
audio {
    width: 70%;
    border-radius: 25px;
    background: #ffe6f0;
    box-shadow: 0 0 10px rgba(255,182,193,0.7);
    margin: 10px auto;
    display: block;
}

/* Footer imut */
footer {
    text-align: center;
    color: #d63384;
    font-size: 20px;
    padding: 10px;
}
</style>

<!-- 🌸 Ornamen bunga & love jatuh -->
<div class="flower">🌸</div>
<div class="flower">💖</div>
<div class="flower">🌺</div>
<div class="flower">💞</div>
<div class="flower">🌷</div>
<div class="flower">💕</div>
""", unsafe_allow_html=True)


# ==========================================================
# 🌷 2. JUDUL & DESKRIPSI
# ==========================================================
st.markdown("<h1>💗 Dashboard Klasifikasi & Deteksi Gambar 💗</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Unggah gambar, pilih model, lalu lihat hasil prediksi AI dengan tampilan lembut dan manis penuh bunga 🌸💖</p>",
    unsafe_allow_html=True
)


# ==========================================================
# 🌼 3. SIDEBAR – PILIHAN MATERI & MODEL
# ==========================================================
st.sidebar.header("🌸 Pilihan Materi")
materi_choice = st.sidebar.selectbox(
    "Pilih materi yang ingin dipelajari:",
    ["Klasifikasi", "Deteksi"]
)

st.sidebar.header("🧠 Pilih Model")
model_choice = st.sidebar.selectbox(
    "Model yang ingin digunakan:",
    ["Klasifikasi 8 kelas", "Deteksi Gender"]
)

# ==========================================================
# 🎵 4. Musik Latar – Cute Pink Style 💖🎀
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

# Pemutar musik yang imut banget 😚💗
st.audio("assets/Cupid.mp3", format="audio/mp3", start_time=0)


# ==========================================================
# 🌺 5. UPLOAD GAMBAR
# ==========================================================
uploaded_file = st.file_uploader("📤 Unggah gambar (JPG/PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Gambar yang diunggah", use_column_width=True)


# ==========================================================
# 🌹 6. LOAD MODEL (CACHED)
# ==========================================================
@st.cache_resource
def load_keras_model():
    """Load model Keras untuk klasifikasi 8 kelas."""
    return load_model("model/klasifikasi 8 kelas.h5")


@st.cache_resource
def load_torch_model():
    """Load model YOLO untuk deteksi gender."""
    return YOLO("model/deteksi gender.pt")


# ==========================================================
# 🌻 7. FUNGSI PREDIKSI
# ==========================================================
def predict_keras(image_input):
    """Prediksi gambar menggunakan model Keras."""
    model = load_keras_model()
    img_resized = image_input.resize((128, 128))
    img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)

    pred = model.predict(img_array)
    class_idx = np.argmax(pred)

    class_labels = [
        "Airplane", "Car", "Cat", "Dog",
        "Flower", "Fruit", "Motorbike", "Person"
    ]
    return class_labels[class_idx], pred[0]


def predict_torch(image_input):
    """Prediksi gambar menggunakan model YOLO (PyTorch)."""
    model = load_torch_model()
    results = model.predict(image_input, imgsz=224, conf=0.5, verbose=False)



    if results[0].boxes is not None and len(results[0].boxes) > 0:
        boxes = results[0].boxes
        cls_idx = int(boxes.cls[0].item())
        conf = float(boxes.conf[0].item())
        label = f"{results[0].names[cls_idx]} ({conf:.2f})"

        st.image(results[0].plot(), caption="🎯 Hasil Deteksi YOLO")
        return label, [conf]

    elif results[0].probs is not None:
        probs = results[0].probs.data.cpu().numpy()
        label_idx = results[0].probs.top1
        return results[0].names[label_idx], probs

    return "Tidak ada deteksi ditemukan", [0.0]


# ==========================================================
# 💖 8. JALANKAN PREDIKSI
# ==========================================================
if uploaded_file:
    if st.button("💫 Jalankan Prediksi Sekarang"):
        with st.spinner("Model sedang bekerja keras dengan penuh cinta... 💕"):
            if model_choice == "Klasifikasi 8 kelas":
                label, prob = predict_keras(image)
            else:
                label, prob = predict_torch(image)

        st.markdown('<div class="result-box fade-in">', unsafe_allow_html=True)
        st.success("✨ Prediksi Berhasil!")
        st.markdown(
            f"<h3>🧾 Label: <span style='color:#d63384;'>{label}</span></h3>",
            unsafe_allow_html=True
        )
        st.bar_chart(prob)
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================================
# 🌼 9. PANDUAN PENGGUNAAN
# ==========================================================
st.markdown("""
**📘 Panduan Penggunaan**
1. Pilih materi: *Klasifikasi* atau *Deteksi*.
2. Pilih model sesuai kebutuhan.
3. Unggah gambar (format JPG atau PNG).
4. Klik **Jalankan Prediksi Sekarang**.
5. Lihat hasil berupa label dan grafik probabilitas.

💡 *Gunakan gambar berukuran kecil agar proses prediksi lebih cepat!*
""")


# ==========================================================
# 🌸 10. PENJELASAN MATERI – DINAMIS BERDASARKAN PILIHAN
# ==========================================================
if materi_choice == "Klasifikasi":
    st.markdown("""
    ### 🌷 Materi: Klasifikasi Gambar

    **Klasifikasi** adalah proses mengenali dan mengelompokkan gambar ke dalam kategori tertentu.  
    Contohnya, sistem AI dapat menentukan apakah gambar yang diunggah adalah *mobil*, *hewan*, atau *manusia*.

    Model yang biasa digunakan untuk klasifikasi antara lain:
    - **CNN (Convolutional Neural Network)**: mengekstraksi fitur penting dari gambar.
    - **Transfer Learning**: memanfaatkan model yang sudah dilatih sebelumnya seperti *VGG16* atau *ResNet*.

    Klasifikasi sering dipakai di bidang:
    - Medis (mendeteksi penyakit dari citra X-ray),
    - Pertanian (mengenali jenis tanaman),
    - Keamanan (membedakan objek berisiko).
    """)

elif materi_choice == "Deteksi":
    st.markdown("""
    ### 🌺 Materi: Deteksi Objek

    **Deteksi objek** berfungsi untuk menemukan dan menandai lokasi suatu objek di dalam gambar.  
    Selain mengetahui *apa* objeknya, sistem juga tahu *di mana* objek tersebut berada.

    Algoritma populer:
    - **YOLO (You Only Look Once)**: cepat dan akurat untuk deteksi waktu nyata.
    - **SSD (Single Shot Multibox Detector)**: efisien untuk perangkat ringan.

    Aplikasi deteksi banyak digunakan untuk:
    - Pemantauan lalu lintas dan keamanan,
    - Deteksi wajah dan emosi,
    - Analisis citra satelit dan drone.
    """)


# ==========================================================
# 🌼 11. ORNAMEN PENUTUP
# ==========================================================
st.markdown("""
<div style='text-align: center; font-size: 22px; margin-top: 30px;'>
    🌷 🌸 💖 🌺 💕 🌼 💗 🌹 🌻
</div>
""", unsafe_allow_html=True)



