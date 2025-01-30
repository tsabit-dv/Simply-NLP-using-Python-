# Chatbot NLP dengan Text-to-Speech (TTS)

Chatbot ini menggunakan **spaCy** untuk pemrosesan bahasa alami (NLP) dan **gTTS (Google Text-to-Speech)** untuk menghasilkan suara dari teks. Program ini berjalan di terminal dan memungkinkan interaksi berbasis suara.

---

## 🚀 Fitur
- **Mendeteksi intent** berdasarkan kata kunci dalam input pengguna.
- **Membalas secara dinamis** dengan respons yang telah ditentukan.
- **Menggunakan Text-to-Speech (TTS)** untuk membacakan respons chatbot.
- **Modular dan scalable**, menggunakan pendekatan berbasis kelas (OOP).

---

## 🛠 Instalasi & Setup

Ikuti langkah-langkah di bawah untuk mengatur chatbot ini di lingkungan virtual Python.

### 1️⃣ **Buat Virtual Environment**
```sh
python -m venv venv
```

### 2️⃣ **Aktifkan Virtual Environment**
- **Windows** (PowerShell):
  ```sh
  venv\Scripts\Activate
  ```
- **macOS/Linux**:
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ **Instal Dependensi**
```sh
pip install -r requirements.txt
```

Jika `requirements.txt` belum ada, buat file tersebut dan tambahkan:
```txt
spacy
gtts
ipython
```

### 4️⃣ **Download Model NLP spaCy**
```sh
python -m spacy download en_core_web_sm
```

---

## 🔧 Cara Menggunakan

Jalankan program dengan perintah:
```sh
python main.py
```

Lalu ikuti instruksi di terminal:
- Ketik pesan untuk berbicara dengan chatbot.
- Ketik `exit` untuk mengakhiri percakapan.

---

## 🔍 Struktur Proyek
```
chatbot_project/
├── main.py         # Kode utama chatbot
├── requirements.txt   # Daftar dependensi
├── README.md          # Dokumentasi proyek
└── venv/              # Virtual environment (tergantung setup)
```

---

## 📌 Catatan
- Jika ada masalah dengan `gTTS`, pastikan Anda memiliki koneksi internet yang stabil.
- Jika ingin menambahkan lebih banyak intent atau respons, edit dictionary `response_rules` dan `responses` di dalam `chatbot.py`.

---

## 📜 Lisensi
Proyek ini bersifat open-source dan dapat digunakan serta dimodifikasi sesuai kebutuhan.

**Selamat mencoba! 🚀**

