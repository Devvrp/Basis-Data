/*
===================================================================
 SKRIP SQL UNTUK DATABASE FIKTIF "TOKO KOPI SENJA" (Versi 2.0)
===================================================================
 - Database ini dirancang untuk bahan tugas visualisasi data.
 - Terdapat 30 baris data transaksi.
 - Kolom baru: 'Metode_Pembayaran' dan 'Rating_Pelanggan'
   untuk analisis yang lebih mendalam.
-------------------------------------------------------------------
*/

-- (Opsional) Hapus tabel jika sudah ada, agar bisa dijalankan berulang kali
DROP TABLE IF EXISTS Data_Penjualan_Kopi;

-- 1. Membuat struktur tabel yang sudah diperbarui
CREATE TABLE Data_Penjualan_Kopi (
    ID_Transaksi INT PRIMARY KEY,
    Tanggal DATE,
    Cabang VARCHAR(50),
    Menu VARCHAR(100),
    Kategori VARCHAR(50),
    Jumlah_Terjual INT,
    Total_Pendapatan INT,
    Metode_Pembayaran VARCHAR(20),
    Rating_Pelanggan INT
);

-- 2. Mengisi data ke dalam tabel (Total 30 data)
INSERT INTO Data_Penjualan_Kopi 
    (ID_Transaksi, Tanggal, Cabang, Menu, Kategori, Jumlah_Terjual, Total_Pendapatan, Metode_Pembayaran, Rating_Pelanggan)
VALUES
    (1001, '2024-11-01', 'Jakarta', 'Kopi Susu Gula Aren', 'Coffee', 120, 3000000, 'QRIS', 5),
    (1002, '2024-11-01', 'Bandung', 'Croissant Coklat', 'Pastry', 80, 2000000, 'QRIS', 4),
    (1003, '2024-11-01', 'Surabaya', 'Americano', 'Coffee', 70, 1750000, 'Tunai', 4),
    (1004, '2024-11-02', 'Jakarta', 'Matcha Latte', 'Non-Coffee', 90, 2700000, 'Debit', 5),
    (1005, '2024-11-02', 'Bandung', 'Kopi Susu Gula Aren', 'Coffee', 110, 2750000, 'QRIS', 5),
    (1006, '2024-11-02', 'Surabaya', 'Red Velvet Latte', 'Non-Coffee', 60, 1800000, 'QRIS', 4),
    (1007, '2024-11-03', 'Jakarta', 'Croissant Coklat', 'Pastry', 85, 2125000, 'Tunai', 3),
    (1008, '2024-11-03', 'Bandung', 'Americano', 'Coffee', 65, 1625000, 'Debit', 4),
    (1009, '2024-11-03', 'Surabaya', 'Kopi Susu Gula Aren', 'Coffee', 130, 3250000, 'QRIS', 5),
    (1010, '2024-11-04', 'Jakarta', 'Americano', 'Coffee', 75, 1875000, 'QRIS', 4),
    (1011, '2024-11-04', 'Bandung', 'Matcha Latte', 'Non-Coffee', 80, 2400000, 'Tunai', 5),
    (1012, '2024-11-04', 'Surabaya', 'Croissant Coklat', 'Pastry', 90, 2250000, 'Debit', 4),
    (1013, '2024-11-05', 'Jakarta', 'Kopi Susu Gula Aren', 'Coffee', 140, 3500000, 'QRIS', 5),
    (1014, '2024-11-05', 'Bandung', 'Red Velvet Latte', 'Non-Coffee', 70, 2100000, 'QRIS', 4),
    (1015, '2024-11-05', 'Surabaya', 'Matcha Latte', 'Non-Coffee', 80, 2400000, 'Tunai', 5),
    (1016, '2024-11-06', 'Jakarta', 'Kopi Susu Gula Aren', 'Coffee', 135, 3375000, 'Debit', 5),
    (1017, '2024-11-06', 'Bandung', 'Americano', 'Coffee', 70, 1750000, 'QRIS', 4),
    (1018, '2024-11-06', 'Surabaya', 'Kopi Susu Gula Aren', 'Coffee', 125, 3125000, 'QRIS', 5),
    (1019, '2024-11-07', 'Jakarta', 'Matcha Latte', 'Non-Coffee', 95, 2850000, 'Tunai', 4),
    (1020, '2024-11-07', 'Bandung', 'Croissant Coklat', 'Pastry', 85, 2125000, 'QRIS', 5),
    (1021, '2024-11-07', 'Surabaya', 'Red Velvet Latte', 'Non-Coffee', 65, 1950000, 'Debit', 3),
    (1022, '2024-11-08', 'Jakarta', 'Croissant Coklat', 'Pastry', 90, 2250000, 'QRIS', 4),
    (1023, '2024-11-08', 'Bandung', 'Kopi Susu Gula Aren', 'Coffee', 115, 2875000, 'Tunai', 5),
    (1024, '2024-11-08', 'Surabaya', 'Americano', 'Coffee', 80, 2000000, 'QRIS', 4),
    (1025, '2024-11-09', 'Jakarta', 'Red Velvet Latte', 'Non-Coffee', 70, 2100000, 'Debit', 4),
    (1026, '2024-11-09', 'Bandung', 'Matcha Latte', 'Non-Coffee', 85, 2550000, 'QRIS', 5),
    (1027, '2024-11-09', 'Surabaya', 'Croissant Coklat', 'Pastry', 95, 2375000, 'Tunai', 4),
    (1028, '2024-11-10', 'Jakarta', 'Kopi Susu Gula Aren', 'Coffee', 150, 3750000, 'QRIS', 5),
    (1029, '2024-11-10', 'Bandung', 'Red Velvet Latte', 'Non-Coffee', 75, 2250000, 'Debit', 4),
    (1030, '2024-11-10', 'Surabaya', 'Matcha Latte', 'Non-Coffee', 85, 2550000, 'QRIS', 5);""