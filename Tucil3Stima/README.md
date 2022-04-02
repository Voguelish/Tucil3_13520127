# Penyelesaian Persoalan 15-Puzzle dengan Algoritma Branch and Bound

i. Deskripsi Singkat Program:
- Program ini dibuat untuk memenuhi tugas kecil 3 IF2211 Strategi Algoritma Semester 2 tahun 2021/2022
- Program merupakan 15-puzzle solver yang menerima input suatu posisi dari 15-puzzle kemudian melakukan pencarian sekuens solusi yang dapat dilakukan untuk mencapai goal state
- Program menggunakan algoritma branch and bound dengan taksiran cost yang digunakan adalah jumlah ubin yang tidak kosong yang tidak berada pada tempat yang sesuai susunan akhir (goal state)
- Program ini menggunakan bahasa python dan library-library dasar python untuk dijalankan
- Program yang dijalankan adalah main.py, yang menggunakan fungsi-fungsi pada branchandbound.py

ii. Requirement Program dan Instalasi Module/Package Tertentu bila ada:
- Terinstal Python pada sistem (lakukan instalasi python pada system bila belum terinstal)
- Menginstall library python yang digunakan pada program:
    1. numpy
    2. time
    3. os
  Install library-library yang digunakan (author menggunakan modul pip untuk menginstal library):
    - Contoh: memasukkan input berupa "pip install numpy" pada cli untuk menginstall library
iii. Langkah Compile Program jika Diperlukan:
- Tidak ada compile program, program cukup dijalankan dengan menggunakan bin/run.bat

iv. Cara Menggunakan Program:
1. Siapkan test case dengan menyimpan file .txt berisi posisi awal 15-puzzle yang ingin di solve pada folder test dalam format file .txt, contoh isi .txt yang valid:
    - 1 3 4
    5 2 6 8
    9 10 7 15
    13 14 12 11
2. Jalankan file run.bat pada folder bin
3. Masukan input berupa nama file test case yang ingin diuji pada program run.bat yang telah dijalankan, kemudian enter
4. Jika unsolvable, program akan menampilkan output bahwa program tidak dapat diselesaikan
5. Jika solvable, program akan melakukan loop pencarian hingga ditemukan solusi dan akan menampilkan output berupa jalan dari simpul awal ke simpul akhir

v. Author / Identitas Pembuat:
- Nama: Adzka Ahmadetya Zaidan
- NIM: 13520127