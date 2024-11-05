# Saat sudah memesan makanan dan minuman, maka transaksi nya sudah tersimpan. 
# Jadi saat ada Tampilan Output "Apakah anda ingin keluar dari program? (y/n): " maka isi 'n' untuk masuk login lainnya admin atau owner buat mengetahui laporan penjualannya.
#Daniel_5803024005

# Data login
login_data = {
    "Pelanggan": {
        "username": "pembeli",
        "password": "123456"
    },
    "Admin": {
        "username": "admin",
        "password": "admin"
    },
    "Pemilik": {
        "username": "owner",
        "password": "654321"
    }
}

# Menu makanan dan minuman
menu_makanan = {
    "Ikan Bakar"  : 13000,
    "Ikan Goreng" : 13000,
    "Ayam Goreng" : 14000,
    "Ayam Bakar"  : 14000,
    "Ayam Geprek" : 15000,
    "Ayam Penyet" : 15000,
    "Sate Kambing": 20000
}

menu_minuman = {
    "Jeruk Hangat" : 3000,
    "Es Lemon"     : 3000,
    "Lemon Hangat" : 4000,
    "Es Teh"       : 4000,
    "Teh Hangat"   : 4000,
    "Es Jeruk"     : 4000,
    "Kopi"         : 4000
}

# Inisialisasi laporan penjualan
laporan_penjualan = []

def login():
    print("\n=== Login Restoran Daniel ===")
    username = input("Username: ")
    password = input("Password: ")
    
    for role, credentials in login_data.items():
        if username == credentials["username"] and password == credentials["password"]:
            print(f"\nLogin berhasil sebagai {role}")
            return role
    
    print("\nUsername atau password salah!")
    return None

# Fungsi untuk menampilkan menu berdasarkan role
def tampilkan_menu(role):
    print("\n=== Menu Restoran Daniel ===")
    if role == "Pelanggan":
        print("1. Tampilkan Menu")
        print("2. Pesan Makanan/Minuman")
        print("q. Keluar")
    elif role == "Admin":
        print("1. Tampilkan Menu")
        print("2. Pesan Makanan/Minuman")
        print("3. Lihat Laporan Penjualan")
        print("4. Lihat Total Pendapatan")
        print("q. Keluar")
    elif role == "Pemilik":
        print("1. Tampilkan Menu")
        print("2. Lihat Laporan Penjualan")
        print("3. Lihat Total Pendapatan")
        print("q. Keluar")
    
    return input("Pilih menu: ")

# Fungsi untuk menampilkan menu makanan dan minuman
def tampilkan_menu_makanan_minuman():
    print("\n=== Menu Makanan ===")
    print("-" * 40)
    print("No. | Makanan           | Harga")
    print("-" * 40)
    for i, (nama, harga) in enumerate(menu_makanan.items(), 1):
        print(f"{i:<4}| {nama:<18} | Rp {harga:,}")
    print("-" * 40)
    
    print("\n=== Menu Minuman ===")
    print("-" * 40)
    print("No. | Minuman           | Harga")
    print("-" * 40)
    for i, (nama, harga) in enumerate(menu_minuman.items(), 1):
        print(f"{i:<4}| {nama:<18} | Rp {harga:,}")
    print("-" * 40)

# Fungsi untuk validasi input numerik
def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Masukkan angka yang valid!")

# Fungsi untuk memesan makanan dan minuman
def pesan_makanan_minuman():
    total_pesanan = 0
    pesanan = []
    
    while True:
        tampilkan_menu_makanan_minuman()
        print("\nPilih jenis pesanan:")
        print("1. Makanan")
        print("2. Minuman")
        print("3. Selesai")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "3":
            break
            
        if pilihan == "1":
            menu_aktif = menu_makanan
            jenis = "Makanan"
        elif pilihan == "2":
            menu_aktif = menu_minuman
            jenis = "Minuman"
        else:
            print("Pilihan tidak valid!")
            continue
            
        nama_menu = input(f"\nMasukkan nama {jenis.lower()}: ")
        
        if nama_menu in menu_aktif:
            try:
                jumlah = input_angka("Jumlah pesanan: ")
                if jumlah <= 0:
                    print("Error: Jumlah harus lebih dari 0!")
                    continue
                    
                harga_satuan = menu_aktif[nama_menu]
                total_harga = harga_satuan * jumlah
                pesanan.append((nama_menu, jenis, harga_satuan, jumlah, total_harga))
                total_pesanan += total_harga
                
                print(f"\n{jenis} ditambahkan: {jumlah} x {nama_menu} = Rp {total_harga:,}")
                print(f"Total pesanan saat ini: Rp {total_pesanan:,}")
            except ValueError:
                print("Error: Masukkan jumlah yang valid!")
        else:
            print(f"Error: {jenis} tidak ditemukan!")
    
    if pesanan:
        print("\n=== Ringkasan Pesanan ===")
        print("-" * 60)
        print("Jenis\t| Menu\t\t| Harga Satuan\t| Jumlah\t| Total")
        print("-" * 60)
        for item in pesanan:
            nama, jenis, harga_satuan, jumlah, total_harga = item
            print(f"{jenis}\t| {nama}\t| Rp {harga_satuan:,}\t| {jumlah}\t| Rp {total_harga:,}")
        print("-" * 60)
        print(f"Total yang harus dibayar: Rp {total_pesanan:,}")
        
        # Proses pembayaran
        while True:
            try:
                uang_bayar = input_angka("Masukkan jumlah uang: Rp ")
                if uang_bayar < total_pesanan:
                    print("Error: Uang tidak cukup!")
                    continue
                kembalian = uang_bayar - total_pesanan
                print(f"Kembalian: Rp {kembalian:,}")
                break
            except ValueError:
                print("Error: Masukkan jumlah uang yang valid!")
        
        # Tambahkan ke laporan penjualan
        laporan_penjualan.extend(pesanan)
        print("\nTransaksi berhasil!")
    else:
        print("\nTidak ada pesanan yang dibuat.")

# Fungsi untuk melihat laporan penjualan
def lihat_laporan_penjualan():
    if not laporan_penjualan:
        print("\nBelum ada penjualan.")
        return
        
    print("\n=== Laporan Penjualan ===")
    print("-" * 70)
    print("No. | Jenis\t| Menu\t\t| Harga Satuan\t| Jumlah\t| Total")
    print("-" * 70)
    
    for i, item in enumerate(laporan_penjualan, 1):
        nama, jenis, harga_satuan, jumlah, total_harga = item
        print(f"{i:<4}| {jenis}\t| {nama}\t| Rp {harga_satuan:,}\t| {jumlah}\t| Rp {total_harga:,}")
    print("-" * 70)

# Fungsi untuk melihat total pendapatan
def lihat_total_pendapatan():
    total = sum(item[4] for item in laporan_penjualan)
    print(f"\nTotal Pendapatan: Rp {total:,}")

# Program utama
def main():
    while True:
        role = login()
        if role is None:
            continue
            
        while True:
            try:
                pilihan = tampilkan_menu(role)

                if role == "Pelanggan":
                    if pilihan == '1':
                        tampilkan_menu_makanan_minuman()
                    elif pilihan == '2':
                        pesan_makanan_minuman()
                    elif pilihan.lower() == 'q':
                        break
                    else:
                        print("Error: Pilihan tidak valid!")
                
                elif role == "Admin":
                    if pilihan == '1':
                        tampilkan_menu_makanan_minuman()
                    elif pilihan == '2':
                        pesan_makanan_minuman()
                    elif pilihan == '3':
                        lihat_laporan_penjualan()
                    elif pilihan == '4':
                        lihat_total_pendapatan()
                    elif pilihan.lower() == 'q':
                        break
                    else:
                        print("Error: Pilihan tidak valid!")
                
                elif role == "Pemilik":
                    if pilihan == '1':
                        tampilkan_menu_makanan_minuman()
                    elif pilihan == '2':
                        lihat_laporan_penjualan()
                    elif pilihan == '3':
                        lihat_total_pendapatan()
                    elif pilihan.lower() == 'q':
                        break
                    else:
                        print("Error: Pilihan tidak valid!")
                        
            except Exception as e:
                print(f"Terjadi kesalahan: {str(e)}")
        
        logout = input("\nApakah anda ingin keluar dari program? (y/n): ")
        if logout.lower() == 'y':
            print("\nTerima kasih telah menggunakan software restoran.")
            break

if __name__ == "__main__":
    main()