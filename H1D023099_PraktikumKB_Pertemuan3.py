import random
from datetime import datetime

def main():
    toko_buku = {
        'nama': "Rowling Bookstore",
        'buku': ['Harry Potter and the Sorcerers Stone', 
                'Harry Potter and the Chamber of Secrets', 
                'Harry Potter and the Order of the Phoenix', 
                'Harry Potter and the Half-Blood Prince', 
                'Harry Potter and the Deathly Hallows'],
        'harga': [250000, 400000, 500000, 380000, 580000],
        'pelanggan': ['Agnes', 'Sophia', 'Rachel', 'Xander', 'Tom']
    }
    
    daftar_hadiah = ['Bookmark Eksklusif', 'Tas Buku', 'Pena Emas', 'Gratis 1 Buku', 'Voucher Rp100.000']
    
    print(f"Selamat datang di {toko_buku['nama']}!")
    nama_pembeli = input("Masukkan nama Anda: ")
    
    if nama_pembeli in toko_buku['pelanggan']:
        print("Anda adalah pelanggan tetap kami!")
 
        hadiah = random.choice(daftar_hadiah)
        print(f"Selamat! Anda mendapatkan hadiah: {hadiah}")
    else:
        print("Anda pelanggan baru, selamat berbelanja!")
        toko_buku['pelanggan'].append(nama_pembeli)
    
    print("\nDaftar Buku Tersedia:")
    buku_harga = list(zip(toko_buku['buku'], toko_buku['harga']))
    [print(f"{i+1}. {buku} - Rp{harga:,}") for i, (buku, harga) in enumerate(buku_harga)]
    
    keranjang = []
    total = 0
    
    while True:
        pilihan = input("\nMasukkan nomor buku yang ingin dibeli (0 untuk selesai): ")
        
        if pilihan == '0':
            break
        
        try:
            index = int(pilihan) - 1
            if 0 <= index < len(toko_buku['buku']):
                keranjang.append(toko_buku['buku'][index])
                total += toko_buku['harga'][index]
                print(f"{toko_buku['buku'][index]} ditambahkan ke keranjang!")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Masukkan angka saja!")
    
    if len(keranjang) > 0:
        print("\n--- Struk Pembelian ---")
        print(f"Tanggal: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"Pembeli: {nama_pembeli}")
        print("\nBuku yang dibeli:")
        for buku in keranjang:
            print(f"- {buku}")
        
        if len(keranjang) >= 3:
            diskon = total * 0.1
            print(f"\nSubtotal: Rp{total:,}")
            print(f"Diskon 10%: Rp{diskon:,}")
            total -= diskon
        
        print(f"\nTotal Bayar: Rp{total:,}")
        
        metode_bayar = input("\nPilih metode pembayaran (Tunai/Debit Card/E-Wallet): ").title()
        while metode_bayar not in ['Tunai', 'Debit Card', 'E-Wallet']:
            print("Pilihan tidak valid. Silakan pilih Tunai/Debit Card/E-Wallet")
            metode_bayar = input("Pilih metode pembayaran: ").title()
        
        print(f"Metode Pembayaran: {metode_bayar}")
        
        nomor_struk = random.randint(1000, 9999)
        print(f"Nomor Struk: #{nomor_struk}")
        
        print("\nTerima kasih telah berbelanja!")
    else:
        print("Anda tidak membeli apapun.")

if __name__ == "__main__":
    main()