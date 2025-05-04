# 🌤️ Personal Daily Dashboard

**Personal Daily Dashboard** adalah aplikasi Python berbasis terminal yang menyajikan:
- Informasi cuaca terkini berdasarkan kota yang dimasukkan pengguna
- 3 berita teknologi terbaru dari negara tersebut
- Kutipan motivasi harian

Aplikasi ini sangat cocok untuk jadi asisten kecil kamu setiap pagi — langsung di terminal! 🚀

---

## 🛠️ Teknologi & Library

- Python 3.x
- [OpenWeatherMap API](https://openweathermap.org/)
- [GNews API](https://gnews.io/)
- [ZenQuotes API](https://zenquotes.io/)
- `requests` - untuk ambil data API
- `colorama` - untuk tampilan warna-warni di terminal

---

## 📦 Instalasi

1. Clone repo atau download file Python-nya

```bash
git clone https://github.com/username/personal-daily-dashboard.git
cd personal-daily-dashboard
```

2. Install dependensi:

```bash
pip install requests colorama
```

---

## 🚀 Cara Menjalankan

```bash
python dashboard.py
```

Lalu ikuti instruksi masukkan nama kota.

---

## 🖥️ Contoh Output

```plaintext
Masukkan nama kota: jakarta

========================================
       Personal Daily Dashboard        
========================================
📍 Lokasi     : Jakarta, ID
🌡️  Suhu      : 30°C (Feels like 33°C)
☁️  Cuaca     : Clear sky ☀️
💧 Kelembapan : 60%
🌬️  Angin     : 4.1 m/s
========================================
📰 Berita Teknologi:
1. Apple Releases New iPhone 17
   https://example.com/news1

2. Robot Revolutionizes Industry
   https://example.com/news2

3. AI Takes Over Manual Tasks
   https://example.com/news3

========================================
💬 Quote of the Day:
"Do one thing every day that scares you." - Eleanor Roosevelt
========================================
```

---

## ⚠️ Catatan

- Pastikan kamu punya koneksi internet saat menjalankan.
- Beberapa API (seperti GNews) punya limit gratis harian.
- Kamu bisa ganti `lang` jadi `id` kalau mau berita dalam Bahasa Indonesia (tapi mungkin hasilnya campur).

---

## 📄 Lisensi

Proyek ini dibuat untuk tujuan belajar dan bebas digunakan ulang ✌️
