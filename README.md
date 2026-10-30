# Sistem Perpustakaan (MVC Application)

## Deskripsi Singkat Aplikasi
Aplikasi Desktop Sistem Perpustakaan ini dibangun menggunakan bahasa pemrograman Python dengan menerapkan arsitektur **MVC (Model-View-Controller)** dan antarmuka grafis berbasis `CustomTkinter`. Aplikasi ini dilengkapi dengan sistem manajemen peran pengguna (*Role-Based Access Control*), enkripsi kata sandi berbasis **SHA-256**, serta integrasi pengujian otomatis (`pytest`) dan CI/CD pipeline menggunakan GitHub Actions.

---

## Struktur Direktori MVC
Proyek ini diorganisasikan ke dalam struktur direktori berikut:

```text
Modul 3/
│
├── .github/workflows/
│   └── ci_pipeline.yml         # Konfigurasi CI/CD GitHub Actions
├── config/
│   └── database.py             # Konfigurasi koneksi database MySQL
├── controllers/
│   ├── anggota_controller.py   # Pengendali data anggota
│   ├── auth_controller.py      # Pengendali autentikasi & login
│   └── buku_controller.py      # Pengendali manajemen buku
├── models/
│   ├── anggota_model.py        # Model data anggota
│   ├── buku_model.py           # Model data buku
│   └── user_model.py           # Model data pengguna & hashing SHA-256
├── views/
│   ├── anggota_view.py         # Tampilan antarmuka anggota
│   ├── buku_view.py            # Tampilan antarmuka buku
│   └── login_view.py           # Tampilan antarmuka login
├── tests/
│   ├── test_auth.py            # Unit test autentikasi
│   └── test_buku.py            # Unit test buku
├── dist/
│   └── AplikasiPerpustakaan.exe # Berkas eksekusi mandiri (standalone app)
├── .gitignore                  # Berkas pengecualian Git
├── main.py                     # Titik masuk utama aplikasi (Entry Point)
├── requirements.txt            # Daftar dependensi pustaka proyek
└── README.md                   # Dokumentasi teknis proyek

## Panduan Instalasi & Konfigurasi Database MySQL

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/abcdNY/Modul3_RPL.git](https://github.com/abcdNY/Modul3_RPL.git)
   cd Modul3_RPL
   