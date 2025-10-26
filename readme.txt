==============================================================
🎯 PROYEK: 💗 Dashboard Klasifikasi & Deteksi Gambar 💗
==============================================================

📘 DESKRIPSI
--------------------------------------------------------------
Aplikasi ini merupakan dashboard interaktif berbasis Streamlit
yang menggabungkan dua model deep learning untuk analisis gambar:

1. Model Klasifikasi (.h5)
   - Berbasis TensorFlow/Keras
   - Mengklasifikasikan gambar ke dalam 8 kelas:
     Airplane ✈, Car 🚗, Cat 🐱, Dog 🐶, Flower 🌸, Fruit 🍎,
     Motorbike 🏍, dan Person 👤

2. Model Deteksi Gender (.pt)
   - Berbasis YOLOv8 (Ultralytics)
   - Mendeteksi jenis kelamin (Laki-laki / Perempuan)
     pada gambar manusia.

Dashboard ini juga dilengkapi tampilan interaktif, musik latar,
dan desain halaman berwarna lembut bertema “Kawaii”.


⚙ CARA MENJALANKAN APLIKASI DI LOKAL
--------------------------------------------------------------
1. Buka terminal di folder proyek:
   Contoh:
   C:\Users\<username>\Documents\SEMESTER 7\big data\UTS Big Data

2. Buat dan aktifkan virtual environment:
   (Windows)
   > python -m venv venv
   > venv\Scripts\activate

   (Mac/Linux)
   $ python3 -m venv venv
   $ source venv/bin/activate

3. Install seluruh dependensi proyek:
   > pip install -r requirements.txt

4. Pastikan file model sudah tersedia di folder:
   - model/klasifikasi 8 kelas.h5
   - model/deteksi gender.pt

5. Jalankan aplikasi Streamlit:
   > streamlit run Masukkan_gambar.py

6. Tunggu hingga muncul URL lokal,
   lalu buka di browser (biasanya):
   http://localhost:8501

7. Untuk menghentikan aplikasi:
   Tekan CTRL + C di terminal.


📁 STRUKTUR FOLDER PROYEK
--------------------------------------------------------------
📦 Ujian-Tengah-Semester-Big-Data
│
├── assets/                  # File statis (gambar, musik, background)
│   ├── Anggiya.jpg
│   ├── background.jpg
│   └── Cupid.mp3
│
├── model/                   # File model deep learning
│   ├── deteksi gender.pt
│   └── klasifikasi 8 kelas.h5
│
├── pages/                   # Halaman tambahan dashboard
│   ├── 1_Materi_Klasifikasi.py
│   ├── 2_Materi_Deteksi.py
│   └── 3_Tentang.py
│
├── sample_images/            # Contoh gambar uji (opsional)
│
├── Masukkan_gambar.py        # File utama aplikasi Streamlit
├── requirements.txt          # Daftar dependensi
├── readme.txt                # Deskripsi proyek
├── .gitignore
├── .gitattributes
├── .python-version
└── venv/                     # Virtual environment lokal (tidak diupload ke GitHub)


🧠 VERSI LIBRARY UTAMA
--------------------------------------------------------------
- Python 3.11
- Streamlit 1.38.0
- TensorFlow-CPU 2.19.0
- Ultralytics 8.3.12
- Torch 2.1.2
- Torchvision 0.16.2
- OpenCV-Python-Headless 4.8.1.78
- Pillow 10.2.0
- NumPy 1.26.4
- Matplotlib 3.8.3


👩🏻‍💻 KONTRIBUTOR
--------------------------------------------------------------
Anggiya Mahara  – Universitas Syiah Kuala  
==============================================================