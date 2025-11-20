#Tugas 4

#--------- Bagian 1 - Dasar Pemrograman Python ---------
# Latihan 1
# Tampilkan kalimat berikut:
# Halo, selamat datang di kelas Python!
print("Halo, selamat datang di kelas Python!")


# Latihan 2
# Buat variabel nama, umur, dan asal.
# Tampilkan dalam format:
# "Nama saya Arif, umur saya 21 tahun, saya berasal dari Balikpapan."
nama = "Arif"
umur = 21
asal = "Balikpapan"

print(f"Nama saya {nama}, umur saya {umur} tahun, saya berasal dari {asal}.")


# Latihan 3
# Buat program yang meminta pengguna memasukkan nama dan umur,
# lalu tampilkan kalimat sapaan menggunakan f-string.
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")

print(f"Halo, {nama}! Senang bertemu dengan Anda yang berumur {umur} tahun.")


# Latihan 4
# Buat program yang menghitung luas persegi panjang.
# Input: panjang dan lebar
# Output: luas
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

luas = panjang * lebar

print(f"Luas persegi panjang adalah: {luas}")


#--------- Bagian 2 - Kondisi dan Percabangan ---------

# Latihan 5
# Minta pengguna memasukkan angka, lalu tampilkan apakah
# angka tersebut positif, negatif, atau nol.
angka = float(input("Masukkan sebuah angka: "))

if angka > 0:
    print("Angka tersebut positif.")
elif angka < 0:
    print("Angka tersebut negatif.")
else:
    print("Angka tersebut adalah nol.")


# Latihan 6
# Minta pengguna memasukkan nilai (0–100)
# dan tampilkan predikat huruf:
# A (>=85), B (70–84), C (55–69), D (<55)
nilai = int(input("Masukkan nilai Anda (0-100): "))

if nilai >= 85:
    print("Predikat: A")
elif nilai >= 70:
    print("Predikat: B")
elif nilai >= 55:
    print("Predikat: C")
else:
    print("Predikat: D")


#--------- Bagian 3 - Perulangan ---------

# Latihan 7
# Tampilkan bilangan ganjil dari 1 sampai 20.
for i in range(1, 21, 2):
    print(i)


# Latihan 8
# Buat program tebak angka sederhana.
# Program menyimpan angka rahasia 7.
# Pengguna diminta menebak sampai benar.
angka_rahasia = 7
tebakan = 0

print("--- Selamat Datang di Game Tebak Angka! ---")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda (1-10): "))
    
    if tebakan < angka_rahasia:
        print("Tebakan terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Tebakan terlalu besar! Coba lagi.")

print(f"Selamat! Anda berhasil menebak angka {angka_rahasia}.")


#--------- Bagian 4 - Struktur Data ---------

# Latihan 9
# Buat list berisi 5 nama teman.
# Tampilkan nama pertama dan terakhir.
nama_teman = ["Andi", "Beni", "Citra", "Dian", "Eka"]

print(f"Nama pertama: {nama_teman[0]}")
print(f"Nama terakhir: {nama_teman[-1]}")


# Latihan 10
# Buat dictionary berisi data diri:
# nama, umur, kota, dan hobi.
# Tampilkan seluruh data dengan loop.
data_diri = {
    "nama": "Budi Santoso",
    "umur": 22,
    "kota": "Surabaya",
    "hobi": "Bermain gitar"
}

print("--- Data Diri ---")
for key, value in data_diri.items():
    print(f"{key.capitalize()}: {value}")


#--------- Bagian 5 - Fungsi ---------

# Latihan 11
# Buat fungsi luas_persegi(sisi) yang mengembalikan nilai luas.
# Panggil fungsi tersebut dengan sisi = 5.
def luas_persegi(sisi):
    return sisi * sisi

sisi_input = 5
hasil_luas = luas_persegi(sisi_input)

print(f"Luas persegi dengan sisi {sisi_input} adalah: {hasil_luas}")


# Latihan 12
# Buat fungsi cek_genap(angka) yang menampilkan
# apakah angka tersebut genap atau ganjil.
def cek_genap(angka):
    if angka % 2 == 0:
        print(f"Angka {angka} adalah GENAP.")
    else:
        print(f"Angka {angka} adalah GANJIL.")

cek_genap(10)
cek_genap(7)
cek_genap(101)


#--------- Bagian 6 - Tugas Mini Project ---------

# Latihan 13
# Buat program kasir sederhana:
# - Input nama barang, harga, dan jumlah
# - Hitung total harga
# - Jika total > 100000, beri diskon 10%
# - Tampilkan total bayar
print("--- Program Kasir Sederhana ---")

nama_barang = input("Masukkan nama barang: ")
harga = float(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah barang: "))

total_harga = harga * jumlah
diskon = 0

if total_harga > 100000:
    diskon = total_harga * 0.10
    print(f"\nSelamat! Anda mendapatkan diskon 10%: Rp {diskon:,.0f}")

total_bayar = total_harga - diskon

print("\n--- Struk Pembayaran ---")
print(f"Nama Barang  : {nama_barang}")
print(f"Harga Satuan : Rp {harga:,.0f}")
print(f"Jumlah       : {jumlah} unit")
print(f"Total Harga  : Rp {total_harga:,.0f}")
print(f"Diskon       : Rp {diskon:,.0f}")
print("------------------------------")
print(f"Total Bayar  : Rp {total_bayar:,.0f}")