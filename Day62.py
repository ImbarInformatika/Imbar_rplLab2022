identitas = {
    "nama" : "imbar",
    "umur" : 19,
    "alamat" : "Malunda"}
identitas2 = {
    "jurusan" : "Informatika",
    "kelas" : "E",
     "hobbi" : "main hp"}


print("identitas : ", identitas)
print()
print("identitas2 : ", identitas2)
print()
hasil = dict(identitas, **identitas2)
print("setelah di gabung : ", hasil)
print()

print(hasil.keys())
print()
print(hasil.values())
