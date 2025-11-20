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