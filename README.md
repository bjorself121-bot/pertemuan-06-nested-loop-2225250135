# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

## Identitas

**Nama:** Muhammad Fatih Ammar  
**NIM:** 2225250135  
**Kelas:** 3E  
**Program Studi:** S1 Pendidikan Matematika  
**Mata Kuliah:** Algoritma dan Pemrograman  

---

## Tujuan

Pertemuan ini bertujuan untuk:

1. Memahami konsep nested loop dalam Python.
2. Membuat pola menggunakan nested loop.
3. Menggunakan akumulasi dalam perulangan.
4. Menggunakan pencacahan dengan kondisi tertentu.
5. Menerapkan nested loop untuk membuat tabel perkalian.
6. Menghitung statistik sederhana dari hasil tabel perkalian.

---

## Struktur Folder

    pertemuan-06-nested-loop-2225250135/
    â”œâ”€â”€ README.md
    â”œâ”€â”€ .gitignore
    â”œâ”€â”€ latihan/
    â”‚   â”œâ”€â”€ 01_pasangan_indeks.py
    â”‚   â”œâ”€â”€ 02_pola_segitiga.py
    â”‚   â”œâ”€â”€ 03_jumlah_per_baris.py
    â”‚   â””â”€â”€ 04_hitung_pasangan.py
    â””â”€â”€ tugas/
        â””â”€â”€ tabel_perkalian_dan_statistik.py

---

## Cara Menjalankan

Program dijalankan menggunakan Python melalui terminal atau Visual Studio Code.

### Menjalankan Latihan 1

    python latihan/01_pasangan_indeks.py

### Menjalankan Latihan 2

    python latihan/02_pola_segitiga.py

### Menjalankan Latihan 3

    python latihan/03_jumlah_per_baris.py

### Menjalankan Latihan 4

    python latihan/04_hitung_pasangan.py

### Menjalankan Tugas 3

    python tugas/tabel_perkalian_dan_statistik.py

---

# Latihan

## Latihan 1 - Pasangan Indeks

File:

    latihan/01_pasangan_indeks.py

Program menampilkan seluruh pasangan `(i, j)` dengan:

- `i = 1..3`
- `j = 1..4`

Program juga menghitung banyak pasangan yang dihasilkan.

Hasil:

    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    Banyak pasangan = 12

Banyak pasangan yang dihasilkan adalah:

    3 Ã— 4 = 12

---

## Latihan 2 - Pola Segitiga

File:

    latihan/02_pola_segitiga.py

Program menerima input `n` dan menghasilkan pola bintang dengan 1 simbol pada baris pertama sampai `n` simbol pada baris ke-n.

Contoh input:

    n: 3

Hasil:

    *
    * *
    * * *

Pada program ini:

- Loop luar digunakan untuk mengatur baris.
- Loop dalam digunakan untuk mencetak jumlah simbol pada setiap baris.
- `print("*", end=" ")` digunakan agar simbol tetap berada pada baris yang sama.
- `print()` digunakan untuk berpindah ke baris berikutnya.

---

## Latihan 3 - Jumlah Per Baris

File:

    latihan/03_jumlah_per_baris.py

Program menghitung jumlah hasil perkalian pada setiap baris.

Hasil:

    Jumlah baris 1 = 6
    Jumlah baris 2 = 12
    Jumlah baris 3 = 18
    Jumlah baris 4 = 24

Contohnya, untuk baris pertama:

    1 Ã— 1 + 1 Ã— 2 + 1 Ã— 3
    = 1 + 2 + 3
    = 6

---

## Latihan 4 - Hitung Pasangan

File:

    latihan/04_hitung_pasangan.py

Program menghitung banyak pasangan `(i, j)` yang memenuhi kondisi:

    i + j <= n

Pengujian:

| Input n | Banyak Pasangan |
|---:|---:|
| 2 | 1 |
| 3 | 3 |
| 5 | 10 |

Contoh untuk `n = 3`, pasangan yang memenuhi kondisi adalah:

    (1, 1)
    (1, 2)
    (2, 1)

Sehingga banyak pasangan adalah:

    3

---

# Tugas 3 - Tabel Perkalian dan Statistik

File:

    tugas/tabel_perkalian_dan_statistik.py

## Deskripsi

Program membuat tabel perkalian berukuran `n Ã— n` menggunakan nested loop.

Program juga menghitung:

1. Total seluruh hasil perkalian.
2. Banyak hasil perkalian yang bernilai genap.
3. Jumlah hasil perkalian pada setiap baris.

Input yang digunakan adalah bilangan bulat positif `n`.

Jika pengguna memasukkan nilai `n` yang tidak positif, program akan meminta input kembali sampai mendapatkan nilai positif.

---

## Algoritma Tugas 3

1. Program meminta pengguna memasukkan nilai `n`.
2. Program memeriksa apakah `n` merupakan bilangan positif.
3. Jika `n <= 0`, program meminta input kembali.
4. `total_semua` diinisialisasi dengan nilai `0`.
5. `count_genap` diinisialisasi dengan nilai `0`.
6. Loop luar menggunakan `i` dari `1` sampai `n`.
7. Pada setiap iterasi loop luar, `total_baris` direset menjadi `0`.
8. Loop dalam menggunakan `j` dari `1` sampai `n`.
9. Program menghitung `hasil = i * j`.
10. Hasil perkalian ditampilkan sebagai bagian dari tabel.
11. `hasil` ditambahkan ke `total_baris`.
12. `hasil` juga ditambahkan ke `total_semua`.
13. Program memeriksa apakah `hasil` merupakan bilangan genap.
14. Jika `hasil` genap, `count_genap` ditambah `1`.
15. Setelah loop dalam selesai, program menampilkan jumlah pada baris tersebut.
16. Setelah seluruh loop selesai, program menampilkan total keseluruhan dan banyak hasil genap.

---

## Peran Variabel dan Loop

### Loop Luar

Loop luar menggunakan variabel `i`.

    for i in range(1, n + 1):

Loop luar berfungsi untuk mengatur baris tabel perkalian.

### Loop Dalam

Loop dalam menggunakan variabel `j`.

    for j in range(1, n + 1):

Loop dalam berfungsi untuk mengatur kolom tabel perkalian.

### Akumulator `total_baris`

    total_baris = 0

Variabel ini digunakan untuk menghitung jumlah hasil perkalian pada setiap baris.

Variabel ini harus direset pada setiap iterasi loop luar agar jumlah setiap baris dihitung secara terpisah.

### Akumulator `total_semua`

    total_semua = 0

Variabel ini digunakan untuk menghitung jumlah seluruh hasil perkalian dari seluruh tabel.

Variabel ini tidak direset pada setiap baris karena harus menyimpan total dari seluruh baris.

### Counter `count_genap`

    count_genap = 0

Variabel ini digunakan untuk menghitung banyak hasil perkalian yang bernilai genap.

Pengecekan dilakukan menggunakan:

    if hasil % 2 == 0:
        count_genap += 1

---

# Hasil Pengujian

Pengujian dilakukan menggunakan tiga nilai `n` yang diwajibkan, yaitu:

- `n = 1`
- `n = 2`
- `n = 3`

## Pengujian 1 - n = 1

Input:

    n: 1

Output:

    Tabel Perkalian dan Statistik
    n: 1
    1       | Jumlah baris 1 = 1

    Total keseluruhan = 1
    Banyak hasil genap = 0

Hasil yang diharapkan:

    Total keseluruhan = 1
    Banyak hasil genap = 0

Hasil aktual sesuai dengan hasil yang diharapkan.

**Status: Berhasil**

---

## Pengujian 2 - n = 2

Input:

    n: 2

Output:

    Tabel Perkalian dan Statistik
    n: 2
    1       2       | Jumlah baris 1 = 3
    2       4       | Jumlah baris 2 = 6

    Total keseluruhan = 9
    Banyak hasil genap = 3

Hasil yang diharapkan:

    Total keseluruhan = 9
    Banyak hasil genap = 3

Hasil aktual sesuai dengan hasil yang diharapkan.

**Status: Berhasil**

---

## Pengujian 3 - n = 3

Input:

    n: 3

Output:

    Tabel Perkalian dan Statistik
    n: 3
    1       2       3       | Jumlah baris 1 = 6
    2       4       6       | Jumlah baris 2 = 12
    3       6       9       | Jumlah baris 3 = 18

    Total keseluruhan = 36
    Banyak hasil genap = 5

Hasil yang diharapkan:

    Total keseluruhan = 36
    Banyak hasil genap = 5

Hasil aktual sesuai dengan hasil yang diharapkan.

**Status: Berhasil**

---

## Rekapitulasi Pengujian

| Input | Total Keseluruhan | Banyak Hasil Genap | Status |
|---:|---:|---:|---|
| 1 | 1 | 0 | Berhasil |
| 2 | 9 | 3 | Berhasil |
| 3 | 36 | 5 | Berhasil |

Seluruh pengujian wajib berhasil dan menghasilkan keluaran sesuai dengan hasil yang diharapkan.

---

# Analisis Efisiensi

Program menggunakan nested loop.

Loop luar berjalan sebanyak `n` kali.

Untuk setiap satu iterasi loop luar, loop dalam juga berjalan sebanyak `n` kali.

Dengan demikian, badan loop dalam berjalan sebanyak:

    n Ã— n = nÂ²

kali.

Pernyataan:

    hasil = i * j

dieksekusi sebanyak `nÂ²` kali.

Contoh:

Jika:

    n = 3

maka:

    3 Ã— 3 = 9

Sehingga pernyataan `hasil = i * j` dieksekusi sebanyak 9 kali.

Ketika nilai `n` semakin besar, jumlah operasi pada nested loop juga semakin besar.

---

# Refleksi Teknis

## 1. Mengapa `total_baris` direset di setiap iterasi loop luar?

`total_baris` digunakan untuk menghitung jumlah hasil perkalian pada satu baris.

Oleh karena itu, nilai `total_baris` harus dikembalikan menjadi `0` ketika berpindah ke baris baru.

Jika tidak direset, jumlah dari baris sebelumnya akan ikut terbawa ke baris berikutnya.

Contohnya:

    Baris 1 = 1 + 2 + 3 = 6

Ketika masuk ke baris kedua, perhitungan harus dimulai kembali dari `0`.

---

## 2. Mengapa `total_semua` tidak direset di setiap baris?

`total_semua` digunakan untuk menyimpan jumlah seluruh hasil perkalian dalam tabel.

Karena itu, nilainya harus terus bertambah dari satu baris ke baris berikutnya.

Jika `total_semua` direset pada setiap baris, maka hasil akhirnya hanya akan menyimpan jumlah dari baris terakhir.

---

## 3. Untuk n, berapa kali pernyataan `hasil = i * j` dieksekusi?

Pernyataan:

    hasil = i * j

dieksekusi sebanyak:

    nÂ²

kali.

Hal tersebut terjadi karena loop luar berjalan `n` kali dan setiap iterasi loop luar menjalankan loop dalam sebanyak `n` kali.

---

## 4. Bagaimana membuktikan `count_genap` benar?

Setiap hasil perkalian diperiksa menggunakan operasi modulus:

    hasil % 2 == 0

Jika hasil bagi sisa 0 ketika dibagi 2, maka hasil tersebut merupakan bilangan genap.

Setiap kali kondisi tersebut terpenuhi:

    count_genap += 1

dijalankan.

Dengan demikian, setiap hasil genap dihitung satu kali.

Sebagai contoh pada `n = 3`, tabel perkaliannya adalah:

    1  2  3
    2  4  6
    3  6  9

Hasil yang genap adalah:

    2, 2, 4, 6, 6

Jumlahnya adalah:

    5

Sehingga:

    Banyak hasil genap = 5

---

## 5. Apa bagian program yang akan paling banyak melakukan operasi ketika n membesar?

Bagian nested loop akan melakukan operasi paling banyak.

Hal ini karena loop tersebut memiliki jumlah eksekusi sebesar:

    nÂ²

Semakin besar `n`, semakin banyak operasi perkalian, penjumlahan, dan pengecekan kondisi yang dilakukan.

---

# Kesimpulan

Pada Pertemuan 06, nested loop digunakan untuk menjalankan sebuah loop di dalam loop lainnya.

Nested loop dapat digunakan untuk:

- Membentuk pasangan indeks.
- Membuat pola.
- Menghitung jumlah pada setiap baris.
- Melakukan pencacahan berdasarkan kondisi.
- Membuat tabel perkalian.
- Menghitung statistik dari hasil perulangan.

Pada Tugas 3, nested loop digunakan untuk membuat tabel perkalian `n Ã— n`. Program juga menerapkan akumulator `total_baris` dan `total_semua`, serta counter `count_genap`.

Berdasarkan pengujian `n = 1`, `n = 2`, dan `n = 3`, program menghasilkan keluaran yang sesuai dengan hasil yang diharapkan.

---

# Refleksi

Kesalahan yang perlu diperhatikan dalam nested loop adalah penempatan variabel akumulator dan counter.

Salah satu kesalahan yang dapat terjadi adalah menempatkan:

    total_semua = 0

