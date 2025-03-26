# Rowling Bookstore Program

## Deskripsi
Program ini merupakan simulasi sistem penjualan di toko buku "Rowling Bookstore". Pengguna dapat membeli buku, mendapatkan hadiah jika mereka adalah pelanggan tetap, serta melakukan pembayaran dengan berbagai metode. Program juga menampilkan struk pembelian setelah transaksi selesai.

## Fitur Utama
1. **Pengenalan Pelanggan:**
   - Jika nama pembeli sudah terdaftar sebagai pelanggan tetap, mereka mendapatkan hadiah.
   - Jika nama pembeli baru, mereka akan ditambahkan ke daftar pelanggan.

2. **Daftar Buku:**
   - Program menampilkan daftar buku yang tersedia beserta harganya.

3. **Proses Pembelian:**
   - Pengguna dapat memilih buku berdasarkan nomor yang ditampilkan.
   - Buku yang dipilih akan ditambahkan ke keranjang belanja.
   - Jika pengguna membeli 3 buku atau lebih, mereka mendapatkan diskon 10%.

4. **Metode Pembayaran:**
   - Pengguna dapat memilih metode pembayaran: Tunai, Debit Card, atau E-Wallet.

5. **Struk Pembelian:**
   - Setelah pembayaran, program mencetak struk pembelian berisi daftar buku, total harga, diskon (jika ada), metode pembayaran, dan nomor struk.

## Cara Menggunakan
1. Jalankan program Python.
2. Masukkan nama pembeli.
3. Pilih buku yang ingin dibeli dengan memasukkan nomor yang tersedia.
4. Setelah selesai memilih, tekan `0`.
5. Pilih metode pembayaran.
6. Struk pembelian akan ditampilkan.

## Teknologi yang Digunakan
- Python
- Modul `random` untuk memilih hadiah pelanggan dan nomor struk acak.
- Modul `datetime` untuk mencetak tanggal dan waktu pembelian.
