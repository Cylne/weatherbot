# 🌦️ Weather & Earthquake

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/your_bot_username)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](#)

Bot Telegram cerdas untuk memberikan informasi cuaca, gempa bumi, curah hujan, kelembaban udara, kelembaban tanah, kecepatan angin, dan temperatur udara secara **real-time**.
Dibuat untuk memudahkan pengguna mendapatkan informasi penting langsung di Telegram dengan tampilan yang simpel, profesional, dan interaktif.



## ✨ Fitur Utama

* 🌍 **Info Gempa Terkini** – Menampilkan data gempa terbaru dari API.
* 🌦️ **Info Cuaca** – Cek cuaca per kota dengan detail:

  * Temperatur
  * Kelembaban udara
  * Kelembaban tanah
  * Curah hujan
  * Kecepatan angin
* 🗂️ **Riwayat Pencarian** – Simpan & tampilkan riwayat info yang pernah dicari.
* 📊 **Statistik Pengguna** – Lacak berapa kali user memakai bot.
* 🏠 **Menu Home, Tentang, & Credits** – Navigasi mudah.
* 📱 **Responsif & Interaktif** – Menggunakan button inline Telegram.



## 🛠️ Tech Stack

* **Bahasa Pemrograman**: Python 3.10+
* **Framework Bot**: [python-telegram-bot v20](https://github.com/python-telegram-bot/python-telegram-bot)
* **Library Pendukung**:

  * `requests` → HTTP request ke API
  * `python-dotenv` → Load konfigurasi dari `.env`



## 📸 Tampilan Bot

Contoh interaksi bot:

```
/start
```

> 🤖 Selamat datang di **Weather & Earthquake Info Bot**
> Pilih menu di bawah ini untuk memulai.



### 📌 Contoh Menu Cuaca

```
Masukkan nama kota: Jakarta
```

Bot akan menjawab:

```
🌤️ Cuaca Jakarta:
🌡️ Temperatur: 30°C
💧 Kelembaban Udara: 75%
🌱 Kelembaban Tanah: 60%
🌧️ Curah Hujan: 10mm
💨 Kecepatan Angin: 5 km/h
```



### 📌 Contoh Menu Gempa

```
/gempa
```

Bot akan menjawab:

```
🌍 Gempa Terkini:
📍 Lokasi: Maluku
📏 Magnitudo: 5.6 SR
📅 Waktu: 08-09-2025 12:34:00
```



## ⚙️ Cara Install & Deploy

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/weatherbot.git
cd weatherbot
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Konfigurasi `.env`

Buat file `.env` di root project:

```
BOT_TOKEN=your-telegram-bot-token
WEATHER_API=https://api.ferdev.my.id/search/cuaca?apikey=your-key
EARTHQUAKE_API=https://api.ferdev.my.id/search/gempa?apikey=your-key
```

### 5️⃣ Jalankan Bot

```bash
python bot.py
```



## 🚀 Deploy ke VPS / Pterodactyl

1. Upload semua file (`bot.py`, `.env`, `requirements.txt`) ke server.
2. Jalankan:

   ```bash
   pip install -r requirements.txt
   python bot.py
   ```
3. Atur **Startup Command** di panel jadi:

   ```bash
   python bot.py
   ```



## 👨‍💻 Credits

* **Development**: [Cylne](https://github.com/Cylne)
* **API Provider**: [ferdev.my.id](https://api.ferdev.my.id)
* **Support & Donasi**: [Saweria](https://saweria.co/CYLNE)



## 📬 Informasi & Kontak

* 📌 Telegram: [@your\_bot\Cylne Project](https://t.me/Cylneee)
* 💻 GitHub: [github.com/Cylne](https://github.com/Cylne)
* ☕ Donasi: [Saweria](https://saweria.co/CYLNE)



## 📝 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
Bebas digunakan, dimodifikasi, dan dikembangkan untuk tujuan belajar maupun produksi.



🔥 Dengan bot ini, pengguna bisa merasakan **teknologi informasi bencana dan cuaca yang praktis & real-time langsung di Telegram**.
