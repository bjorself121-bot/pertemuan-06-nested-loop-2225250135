# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi statistik
total_semua = 0
count_genap = 0

# Nested loop untuk membuat tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(hasil, end="\t")

        # Hitung total per baris
        total_baris += hasil

        # Hitung total keseluruhan
        total_semua += hasil

        # Hitung banyak hasil yang genap
        if hasil % 2 == 0:
            count_genap += 1

    print(f"| Jumlah baris {i} = {total_baris}")

print()
print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")