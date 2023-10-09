from prettytable import PrettyTable

# isi tabel menu
tabel_menu = PrettyTable()
tabel_menu.field_names = ["No.", "Menu", "Jenis Menu", "Harga"]
tabel_menu.add_row(["1", "Sup Jagung Manis", "Sup", "Rp.10,000"])
tabel_menu.add_row(["2", "Sup Wantan", "Sup", "Rp.12,000"])
tabel_menu.add_row(["3", "Sup Ayam Pedas", "Sup", "Rp.15,000"])
tabel_menu.add_row(["4", "Bakpao", "Dimsum", "Rp.5000"])
tabel_menu.add_row(["5", "Siomay", "Dimsum", "Rp.5000"])
tabel_menu.add_row(["6", "Lumpia", "Dimsum", "Rp.5000"])
tabel_menu.add_row(["7", "Mie Goreng", "Mie", "Rp.20,000"])
tabel_menu.add_row(["8", "Kwetiau Goreng", "Mie", "Rp.20,000"])
tabel_menu.add_row(["9", "Mihun Goreng", "Mie", "Rp.20,000"])
tabel_menu.add_row(["10", "Nasi Goreng", "Nasi", "Rp.20,000"])
tabel_menu.add_row(["11", "Nasi Hainam", "Nasi", "Rp.20,000"])
tabel_menu.add_row(["12", "Ayam Kung Pao", "Daging", "Rp.25,000"])
tabel_menu.add_row(["13", "Bebek Goreng", "Daging", "Rp.25,000"])
tabel_menu.add_row(["14", "Sapi Lada Hitam", "Daging", "Rp.30,000"])
tabel_menu.add_row(["15", "Ikan Asam Manis", "Seafood", "Rp.20,000"])
tabel_menu.add_row(["16", "Udang Saos Tiram", "Seafood", "Rp.25,000"])
tabel_menu.add_row(["17", "Kepiting Saos Tiram", "Seafood", "Rp.40,000"])
tabel_menu.add_row(["18", "Ikan Goreng", "Daging", "Rp.30,000"])
tabel_menu.add_row(["19", "Tumis Brokoli", "Sayur", "Rp.10,000"])
tabel_menu.add_row(["20", "Cap Cai", "Sayur", "Rp.10,000"])
tabel_menu.add_row(["21", "Hot Pot Daging Sapi", "Hot Pot", "Rp.30,000"])
tabel_menu.add_row(["22", "Hot Pot Ikan", "Hot Pot", "Rp.25,000"])
tabel_menu.add_row(["23", "Hot Pot Sayuran", "Hot Pot", "Rp.20,000"])
tabel_menu.add_row(["24", "Teh Hijau", "Minuman", "Rp.5000"])
tabel_menu.add_row(["25", "Es Jeruk", "Minuman", "Rp.5000"])
tabel_menu.add_row(["26", "Jus Mangga", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["27", "Jus Alpukat", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["28", "Jus Apel", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["29", "Jus Nangka", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["30", "Jus Naga", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["31", "Jus Sirsak", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["32", "Jus Nanas", "Minuman", "Rp.10,000"])
tabel_menu.add_row(["33", "Rolade Saus Hoisin", "Cemilan", "Rp.15,000"])
tabel_menu.add_row(["34", "Telur Puyuh Kecap", "Cemilan", "Rp.15,000"])
tabel_menu.add_row(["35", "Tanghulu", "Cemilan", "Rp.5,000"])
tabel_menu.add_row(["36", "Tangyuan", "Cemilan", "Rp.10,000"])
tabel_menu.add_row(["37", "Bubur Ketan Hitam", "Cemilan", "Rp.10,000"])
tabel_menu.add_row(["38", "Mooncake", "Cemilan", "Rp.10,000"])
tabel_menu.add_row(["39", "Douhua", "Cemilan", "Rp.10,000"])
tabel_menu.add_row(["40", "Osmanthus Jelly", "Cemilan", "Rp.10,000"])

# Loop untuk menampilkan menu kepada pelanggan
def menu_pelanggan():
    print
    print("\nBerikut Menu Restoran Chinese Moon House:\n")
    print(tabel_menu)

# Loop untuk pelanggan memesan menu
def pesan_menu_pelanggan():
    pesanan = []  # Membuat daftar pesanan
    menu_pelanggan()  # Menampilkan menu pertama kali

    while True:
        nomor_menu = input("\nMasukkan nomor menu yang ingin dipesan (pilih sesuai nomor menu untuk memesan, pilihan s untuk selesai dan pesan): ")
        
        if nomor_menu == "s":
            if len(pesanan) == 0:
                print("Anda belum memesan apa-apa.")
                print("\nTerima kasih telah datang ke Restoran Kami! Silahkan Datang Kembali.")
                exit()
            else:
                print("\nBerikut pesanan Anda:\n")
                for pesanan_menu in pesanan:
                    print(pesanan_menu)
                print("\nTerima kasih telah melakukan pemesanan! Silahkan Datang Kembali.")
                exit()
        elif nomor_menu.isnumeric() and 1 <= int(nomor_menu) <= len(tabel_menu._rows):
            nomor_menu = int(nomor_menu)
            menu = tabel_menu._rows[nomor_menu - 1][1]  # Kolom kedua adalah kolom "Menu"
            pesanan.append(menu)
            print(f"{menu} berhasil ditambahkan ke pesanan Anda.")
        else:
            print("Menu tidak valid. Silakan masukkan nomor menu yang benar.")



# Loop untuk mengedit menu oleh manajer restoran
def menu_manajer():
    while True:
        print("\nMenu Manajer Chinese Moon House:")
        print("1. Tampilkan Menu")
        print("2. Tambahkan Menu")
        print("3. Edit Menu")
        print("4. Hapus Menu")
        print("5. Keluar")

        pilihan = input("Pilih tindakan (1/2/3/4/5): ")

        if pilihan == "1":
            print(tabel_menu)
        elif pilihan == "2":
            nomor = input("Masukkan nomor menu baru: ")
            menu = input("Masukkan nama menu baru: ")
            jenis = input("Masukkan jenis menu: ")
            harga = input("Masukkan harga menu: ")
            tabel_menu.add_row([nomor, menu, jenis, harga])
            print("Menu berhasil ditambahkan.")
        elif pilihan == "3":
            nomor_menu = input("Masukkan nomor menu yang ingin diedit: ")
            indeks = tabel_menu.field_names.index("No.")
            for row in tabel_menu._rows:
                if row[indeks] == nomor_menu:
                    menu = input("Masukkan nama menu baru: ")
                    jenis = input("Masukkan jenis menu baru: ")
                    harga = input("Masukkan harga menu baru: ")
                    row[1] = menu
                    row[2] = jenis
                    row[3] = harga
                    print("Menu berhasil diedit.")
                    break
            else:
                print("Menu tidak ditemukan.")
        elif pilihan == "4":
            nomor_menu = input("Masukkan nomor menu yang ingin dihapus: ")
            indeks = tabel_menu.field_names.index("No.")
            new_rows = []
            for row in tabel_menu._rows:
                if row[indeks] != nomor_menu:
                    new_rows.append(row)
            tabel_menu._rows = new_rows
            print("Menu berhasil dihapus.")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Loop utama program
def tampilan_awal():
    while True:
        print("\nSelamat datang di Chinese Moon House!")
        print("1. Pelanggan Restoran")
        print("2. Manajer Restoran")
        print("3. Keluar Restoran")
        role = input("Disini anda sebagai? (1/2/3): ")

        if role == "1":
            print("=" * 32)
            print("Selamat datang di restoran kami!")
            print("=" * 32)
            pesan_menu_pelanggan()
        elif role == "2":
            print("=" * 41)
            print("Selamat datang kembali Bapak/Ibu Manager!")
            print("=" * 41)
            menu_manajer()
        elif role == "3":
            print("Terimakasih atas kunjungannya, Silahkan datang lagi!")
            break
        else:
            print("Peran tidak valid. Silakan coba lagi.")

# Untuk mengeksekusi bagian tampilan awal terlebih dahulu tanpa membaca baris program diatas yang lain
if __name__ == "__main__":
    tampilan_awal()
