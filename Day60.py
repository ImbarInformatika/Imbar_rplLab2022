identitas = {
    "nama" : "imbar",
    "umur" : 19,
    "alamat" : "Malunda"}

print(identitas)


identitas["umur"] = 20;
print("umur : ", identitas["umur"])#mengubah nilai nama

del identitas["nama"]#mengapus properti nama dan valuenya 
print("setelah menggunakan del : ", identitas)

identitas.clear()#menghapus semua properti dictionary
print("setelah menggunakan clear : ", identitas)
