# e-Library

## Deskripsi
Proyek **e-Library** adalah sebuah aplikasi berbasis web yang dikembangkan menggunakan **Django** untuk mengelola koleksi buku dalam format PDF. Aplikasi ini memungkinkan pengguna untuk mengunggah, mengedit, menghapus, serta menandai buku sebagai favorit. Selain itu, pengguna juga memiliki profil yang dapat diperbarui.

## Teknologi yang Digunakan
- **Backend**: Django 5.x
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, JavaScript (template rendering dengan Django)
- **File Handling**: Django FileSystemStorage
- **PDF Processing**: PyMuPDF (pymupdf)
- **Authentication**: Django Authentication

## Instalasi dan Menjalankan Proyek
### 1. Clone Repository
```sh
https://github.com/username/elibrary.git
cd elibrary
```

### 2. Buat Virtual Environment dan Install Dependensi
```sh
python -m venv .venv
source .venv/bin/activate  # Untuk Mac/Linux
.venv\Scripts\activate    # Untuk Windows
```

### 3. Jalankan Migrasi Database
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4. Buat Superuser (Opsional)
```sh
python manage.py createsuperuser
```

### 5. Jalankan Server
```sh
python manage.py runserver
```

Akses aplikasi di **http://127.0.0.1:8000/**

## Catatan Penting
- Semua file PDF yang diunggah akan disimpan di dalam folder `media/pdfs/`.
- Gambar hasil konversi dari PDF akan disimpan di dalam `media/images/`.
- Pastikan folder `media/` memiliki izin baca/tulis agar file dapat disimpan.
