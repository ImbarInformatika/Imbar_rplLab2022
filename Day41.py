nama = []
batas = int(input("masukkan batas data : "))

while True:
    baru = input("Masukkan nama yang ingin di tambahkan : ")
    nama.append(baru)

    print(nama)
    print("banyaknya data : ", len(nama))
    if len(nama) == batas:
        break
