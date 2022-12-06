nomor = [4, 7, 2, 8, 9]

print("list saat ini : ", nomor)

print()
cek_index = int(input("masukkan nomor yang akan di cek : "))

if cek_index in nomor:
    print(cek_index, "ada di index", nomor.index(cek_index))

else:
    print(cek_index, "tidak di dalam index")
