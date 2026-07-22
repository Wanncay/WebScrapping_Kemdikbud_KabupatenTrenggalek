# Web Scraping Data Sekolah Kabupaten Trenggalek

Proyek ini merupakan aplikasi **web scraping berbasis Python dan Selenium** untuk mengambil data sekolah dari situs resmi **Dapodik Kementerian Pendidikan Dasar dan Menengah**.

Program mengambil data sekolah dari seluruh kecamatan di Kabupaten Trenggalek, kemudian menggabungkan data utama sekolah dengan informasi alamat dan koordinat geografis. Hasil akhir disimpan dalam format Excel agar dapat digunakan untuk analisis data, visualisasi, pemetaan sekolah, atau pengembangan dashboard pendidikan.

---

## Tujuan Proyek

Proyek ini dibuat untuk:

- Mengotomatisasi pengambilan data sekolah di Kabupaten Trenggalek.
- Mengumpulkan data sekolah dari seluruh jenjang pendidikan yang tersedia.
- Mengambil informasi jumlah peserta didik, rombongan belajar, dan guru.
- Mengambil informasi alamat serta koordinat lokasi sekolah.
- Menyimpan seluruh hasil scraping ke dalam satu file Excel.
- Menyediakan dataset yang dapat digunakan untuk analisis pendidikan dan pemetaan sekolah.

---

## Teknologi yang Digunakan

- **Python**
- **Selenium**
- **Pandas**
- **Google Chrome**
- **ChromeDriver**
- **Microsoft Excel**

---

## Sumber Data

Data diambil dari halaman satuan pendidikan pada situs Dapodik:

```text
https://dapo.dikdasmen.go.id/
```

Program menggunakan halaman daftar satuan pendidikan untuk setiap kecamatan di Kabupaten Trenggalek.

---

## Wilayah yang Diambil

Program melakukan scraping pada 14 kecamatan di Kabupaten Trenggalek:

1. Panggul
2. Trenggalek
3. Pule
4. Dongko
5. Watulimo
6. Munjungan
7. Durenan
8. Gandusari
9. Tugu
10. Pogalan
11. Karangan
12. Bendungan
13. Suruh
14. Kampak

---

## Data yang Dikumpulkan

### Data Utama Sekolah

Data utama diambil dari tabel daftar satuan pendidikan:

| Kolom | Keterangan |
|---|---|
| Kecamatan | Kecamatan lokasi sekolah |
| Nama Sekolah | Nama satuan pendidikan |
| NPSN | Nomor Pokok Sekolah Nasional |
| BP | Bentuk pendidikan atau jenjang sekolah |
| Status | Status sekolah negeri atau swasta |
| PD | Jumlah peserta didik |
| Rombel | Jumlah rombongan belajar |
| Guru | Jumlah guru |
| URL | Tautan halaman detail sekolah |

### Data Detail Kontak

Program membuka halaman detail setiap sekolah dan mengambil informasi dari tab **Kontak**:

| Kolom | Keterangan |
|---|---|
| Alamat Lengkap | Alamat sekolah |
| RT/RW | Nomor RT dan RW |
| Dusun | Nama dusun |
| Desa/Kelurahan | Desa atau kelurahan sekolah |
| Kecamatan Detil | Kecamatan berdasarkan halaman detail |
| Kabupaten | Kabupaten lokasi sekolah |
| Provinsi | Provinsi lokasi sekolah |
| Kode Pos | Kode pos sekolah |
| Lintang | Koordinat latitude |
| Bujur | Koordinat longitude |

---

## Alur Kerja Program

```text
Menjalankan Google Chrome
        ↓
Membuka halaman sekolah setiap kecamatan
        ↓
Memilih semester 2024/2025 Ganjil
        ↓
Memilih seluruh jenjang pendidikan
        ↓
Mengambil data sekolah dari tabel
        ↓
Membuka halaman detail setiap sekolah
        ↓
Membuka tab Kontak
        ↓
Mengambil alamat dan koordinat sekolah
        ↓
Menggabungkan seluruh data
        ↓
Menyimpan hasil ke file Excel
```

---

## Fitur Utama

- Scraping data sekolah dari 14 kecamatan secara otomatis.
- Pemilihan semester melalui elemen dropdown pada halaman web.
- Pemilihan seluruh jenjang pendidikan.
- Pengambilan data dari tabel sekolah.
- Pengambilan halaman detail untuk setiap sekolah.
- Penggunaan `WebDriverWait` untuk menunggu elemen tersedia.
- Penanganan error menggunakan `try-except` agar proses tidak langsung berhenti.
- Penyimpanan hasil scraping ke dalam format `.xlsx`.

---

## Struktur Proyek

```text
web-scraping-kemdikbud-trenggalek/
│
├── All Kemdikbud.py
├── data_semua_sekolah_trenggalek_ganjil.xlsx
├── requirements.txt
└── README.md
```

Keterangan:

- `All Kemdikbud.py` merupakan program utama web scraping.
- `data_semua_sekolah_trenggalek_ganjil.xlsx` merupakan hasil scraping.
- `requirements.txt` berisi daftar library Python.
- `README.md` berisi dokumentasi proyek.

---

## Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/web-scraping-kemdikbud-trenggalek.git
cd web-scraping-kemdikbud-trenggalek
```

Ganti `username` dengan username GitHub Anda.

### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```bash
venv\Scripts\activate
```

Aktifkan pada Linux atau macOS:

```bash
source venv/bin/activate
```

### 3. Instalasi Library

```bash
pip install selenium pandas openpyxl
```

Atau menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isi file `requirements.txt`:

```text
selenium
pandas
openpyxl
```

---

## Persiapan ChromeDriver

Pastikan Google Chrome telah terpasang. Selenium versi terbaru umumnya dapat mengelola driver secara otomatis melalui Selenium Manager.

Periksa versi Selenium:

```bash
pip show selenium
```

Perbarui Selenium apabila diperlukan:

```bash
pip install --upgrade selenium
```

---

## Cara Menjalankan Program

Jalankan perintah berikut melalui terminal:

```bash
python "All Kemdikbud.py"
```

Setelah program dijalankan:

1. Google Chrome akan terbuka secara otomatis.
2. Program mengunjungi halaman sekolah setiap kecamatan.
3. Semester **2024/2025 Ganjil** akan dipilih.
4. Program memilih opsi **Semua Jenjang**.
5. Data sekolah akan diambil dari tabel.
6. Program membuka detail setiap sekolah dan mengambil data kontak.
7. Hasil disimpan ke dalam file Excel.

---

## Output

Program menghasilkan file:

```text
data_semua_sekolah_trenggalek_ganjil.xlsx
```

Contoh struktur data hasil scraping:

| Kecamatan | Nama Sekolah | NPSN | BP | Status | PD | Rombel | Guru | Desa/Kelurahan | Lintang | Bujur |
|---|---|---:|---|---|---:|---:|---:|---|---:|---:|
| Kec. Trenggalek | Contoh Sekolah | 12345678 | SD | Negeri | 250 | 12 | 18 | Sumbergedong | -8.xxxx | 111.xxxx |

Data pada tabel di atas hanya merupakan contoh struktur, bukan hasil asli scraping.

---

## Penjelasan Fungsi Utama

### `pilih_semester()`

Fungsi ini memilih semester **2024/2025 Ganjil** melalui dropdown dengan ID `selectSemester`.

### `pilih_semua_jenjang()`

Fungsi ini memilih seluruh jenjang sekolah melalui dropdown dengan ID `selectJenjang`. Program terlebih dahulu memilih jenjang SMP untuk memicu perubahan halaman, kemudian memilih opsi Semua Jenjang.

### `extract_sekolah_links()`

Fungsi ini mengambil data sekolah dari tabel, seperti nama sekolah, NPSN, bentuk pendidikan, status, jumlah peserta didik, rombongan belajar, jumlah guru, dan URL halaman detail sekolah.

### `extract_kontak()`

Fungsi ini membuka tab Kontak pada halaman detail sekolah dan mengambil data alamat, wilayah administrasi, kode pos, serta koordinat lintang dan bujur.

### Proses Utama

Program melakukan perulangan pada seluruh kecamatan, mengambil daftar sekolah, mengambil detail kontak setiap sekolah, menggabungkan data, lalu menyimpannya menggunakan Pandas.

---

## Penanganan Error

Program menggunakan blok `try-except` pada beberapa bagian penting, seperti:

- Pemilihan semester.
- Pemilihan jenjang pendidikan.
- Pengambilan data sekolah dari tabel.
- Pengambilan detail kontak sekolah.

Apabila salah satu sekolah gagal diproses, program akan menampilkan pesan error dan melanjutkan proses ke sekolah berikutnya.

---

## Kendala yang Mungkin Terjadi

### Elemen Tidak Ditemukan

Struktur HTML situs Dapodik dapat berubah sehingga selector seperti ID, XPath, atau CSS Selector mungkin tidak lagi sesuai.

### Koneksi Internet Lambat

Halaman sekolah dan tab kontak membutuhkan waktu untuk dimuat. Apabila koneksi lambat, nilai timeout pada `WebDriverWait` dapat ditambah.

### Proses Berjalan Lama

Program membuka halaman detail setiap sekolah satu per satu. Semakin banyak sekolah, semakin lama proses scraping berlangsung.

### File Excel Sedang Dibuka

Pastikan file hasil Excel tidak sedang dibuka ketika program dijalankan ulang agar tidak terjadi error saat penyimpanan.

---

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Menambahkan mode headless agar browser berjalan di latar belakang.
- Menambahkan progress bar menggunakan `tqdm`.
- Menyimpan data sementara agar proses dapat dilanjutkan jika terhenti.
- Menambahkan validasi data kosong dan data duplikat.
- Menyimpan hasil ke CSV atau database.
- Membuat dashboard menggunakan Excel, Power BI, atau Streamlit.
- Membuat peta persebaran sekolah berdasarkan koordinat lintang dan bujur.
- Menambahkan logging ke dalam file.
- Mengubah semester menjadi parameter yang dapat dipilih pengguna.
- Mengoptimalkan waktu tunggu agar scraping lebih cepat.

---

## Potensi Analisis Data

Dataset hasil scraping dapat digunakan untuk:

- Membandingkan jumlah sekolah antar kecamatan.
- Menganalisis distribusi sekolah negeri dan swasta.
- Menganalisis rasio peserta didik terhadap guru.
- Menganalisis rata-rata peserta didik per rombongan belajar.
- Mengetahui kecamatan dengan jumlah sekolah terbanyak.
- Memetakan persebaran sekolah berdasarkan koordinat geografis.
- Mengidentifikasi wilayah yang memiliki fasilitas pendidikan terbatas.

Contoh metrik lanjutan:

```text
Rasio Siswa per Guru = Jumlah Peserta Didik / Jumlah Guru

Rasio Siswa per Rombel = Jumlah Peserta Didik / Jumlah Rombel
```

---

## Etika Penggunaan

Proyek ini dibuat untuk tujuan pembelajaran, portofolio, dan analisis data pendidikan.

Pengguna disarankan untuk:

- Tidak mengirim permintaan ke server secara berlebihan.
- Memberikan jeda antarpermintaan.
- Mematuhi ketentuan penggunaan situs sumber.
- Tidak menggunakan data untuk tujuan yang merugikan.
- Mencantumkan sumber data saat dataset digunakan atau dipublikasikan.

---

## Catatan

Struktur halaman Dapodik dapat berubah sewaktu-waktu. Apabila program tidak berjalan, periksa kembali selector HTML yang digunakan pada Selenium.

Data yang diperoleh juga mengikuti data yang tersedia pada semester yang dipilih di situs sumber.

---

## Author

**Ridhwan Fachrul Arief**

Project ini dibuat sebagai bagian dari portofolio di bidang:

- Data Collection
- Web Scraping
- Data Engineering
- Data Analysis
- Automation with Python

---

## Lisensi

Proyek ini dapat digunakan untuk pembelajaran dan pengembangan portofolio dengan tetap mencantumkan sumber data.
