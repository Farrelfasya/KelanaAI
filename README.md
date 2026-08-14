# KelanaAI

AI Travel Planner — dibangun dengan Python, Next.js, dan Amazon Bedrock.

## Sesi 1: Trip Summary Generator (Console App)

Fitur pertama KelanaAI adalah aplikasi konsol Python sederhana untuk mencatat
dan menampilkan ringkasan rencana perjalanan pengguna.

### Struktur Proyek

```
kelana-ai/
├── README.md
├── backend/
│   └── main.py
└── frontend/
    └── .gitkeep
```

### Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
cd backend
python main.py
```

Program akan meminta input berikut:

- `destination` — nama kota/destinasi (string)
- `country` — nama negara (string)
- `days` — jumlah hari perjalanan (integer)
- `budget` — anggaran perjalanan (float)
- `currency` — mata uang (string)
- `travel_month` — bulan perjalanan (string)

Contoh output:

```
========================
      KelanaAI
========================
Destination : Japan
Country     : Japan
Days        : 5
Budget      : 1500 USD
Currency    : USD
Travel Month: December
========================
```

## Roadmap

- [x] Sesi 1: Trip Summary Generator (console app)
- [ ] Sesi 2: Integrasi frontend Next.js
- [ ] Sesi 3: Integrasi Amazon Bedrock untuk rekomendasi perjalanan berbasis AI
