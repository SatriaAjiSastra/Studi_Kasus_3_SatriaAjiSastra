daftar_buku = (
    "Engineer", 
    "Laskar Pelangi", 
    "Cryptography", 
    "Pemrograman", 
    "Ilmu Komputer"
)

pinjaman_peter = []

print("Perpustakaan Fakultas Teknik")
print()
print("Daftar Buku yang Tersedia:")
for buku in daftar_buku:
    print("- " + buku)

while True:
    print()
    print("Menu: [1] Pinjam  [2] Hapus Pinjaman  [3] Selesai")
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        buku_dipinjam = input("Masukkan judul buku yang dipinjam: ")
        
        if buku_dipinjam in daftar_buku:
            print("buku berhasil dipinjam")
            pinjaman_peter.append(buku_dipinjam) 
        else:
            print("buku tidak tersedia")
            
    elif pilihan == '2':
        print("Pinjaman Anda saat ini:", pinjaman_peter)
        buku_dihapus = input("Masukkan judul buku yang ingin dihapus: ")
        
        if buku_dihapus in pinjaman_peter:
            pinjaman_peter.remove(buku_dihapus)
            print("Buku berhasil dihapus dari pinjaman.")
        else:
            print("Buku tersebut tidak ada di keranjang pinjaman Anda.")
            
    elif pilihan == '3':
        break
        
    else:
        print("Pilihan tidak valid.")

print()
print("=== Seluruh Buku yang Dipinjam Peter ===")
if len(pinjaman_peter) > 0:
    for buku in pinjaman_peter:
        print("- " + buku)
else:
    print("Tidak ada buku yang dipinjam.")