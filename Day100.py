#membuat peminjaman buku sederhana

buku = ["dasar dasar pemrograman", "aljabar linear", "algoritma dan struktur data", "pengembangan multimedia", "dasar dasar microsoft word 2010", "matematika diskrit", "tips dan trik power point"]

print('''<=====> BUKU YANG SEDANG TERSEDIA <=====>
1. Dasar Dasar Pemrograman
2. Aljabar Linear
3. Algoritma dan Struktur Data
4. Pengembangan Multimedia
5. Dasar Dasar Microsoft Word 2010
6. Matematika Diskrit
7. Tips dan Trik Power Point''')


print()
print()
print()


print("<====> PENGISIAN IDENTITAS PEMINJAM <====>")
print()
nama = input("Masukkan nama peminjam : ").lower()
pinjam = input("Masukkan Buku yang akan di pinjam : ").lower()
print()

print("<====> STATUS PEMINJAMAN <====>")
print()
if pinjam in buku:
	print(f'''buku {pinjam} berhasil dj pinjam oleh {nama}''')
	print()
	print(f'''Saudara {nama} Anda akan
meminjam buku {pinjam}
selama 7 hari''')
	
else:
	print(f'''mohon maaf buku {pinjam} sedang kosong''')

print()


print("TERIMAH KASIH")
print("SELAMAT DATANG KEMBALI")