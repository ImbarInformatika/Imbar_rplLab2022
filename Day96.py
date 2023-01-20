#Program untuk menampilkan informasi buku

buku = {
    "judul": "Pemrograman Dasar",
    "pengarang": "Musliadi KH",
    "tahun_terbit": 2019
}

def info_buku():
  print(f"Judul buku   : {buku['judul']}")
  print(f"Pengarang    : {buku['pengarang']}")
  print(f"Tahun terbit : {buku['tahun_terbit']}")

info_buku()