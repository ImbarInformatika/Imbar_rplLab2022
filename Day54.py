angka = [7, 4, 1, 6, 20]
print("sebelum ada perubahan : ", angka)

del angka[3] #Menghapus angka yang berada pada index ke tiga
print("setelah mengunakan del : ", angka)

hapus = int(input("masukkan angka yang akan dihapus : "))
angka.remove(hapus) #menghapus data berdasarkan angka yang di inputkan 
print("setelah mengunakan remove : ", angka)


data = angka.pop() #menghapus data pada bagian akhir
print("setelah mengunakan pop : ", angka)
