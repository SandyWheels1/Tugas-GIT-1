Assignment Detail

Pada tugas kali ini, kita akan membersihkan data marketing_data.csv menggunakan prinsip OOP.

Prinsip OOP yang akan digunakan:

Basic OOP
Inheritance
Polymorphism
Script dapat menggunakan pandas agar lebih mudah mengerjakan.

Task 1: Basic OOP

Buatlah class MarketingDataETL yang memiliki tiga metode:

1.extract(): akan membaca data dari sebuah file CSV (Misalkan, marketing_data.csv)
2.transform(): akan melakukan pembersihan dan transformasi sederhana pada data (seperti mengubah format tanggal atau membersihkan nilai yang kosong)
3.store(): akan menyimpan data yang telah ditransformasi ke dalam struktur data DataFramet.

Task 2: Inheritance & Polymorphism

1.Gunakan inheritance untuk membuat class TargetedMarketingETL yang mewarisi dari MarketingDataETL.
2.Tambahkan metode segment_customers() yang mengelompokkan pelanggan berdasarkan kriteria tertentu (misalnya, pengeluaran total atau kategori produk yang dibeli).
3.Demonstrasi polymorphism dengan meng-override metode transform() dalam TargetedMarketingETL untuk menambahkan logika segmentasi pelanggan ke dalam proses transformasi.
