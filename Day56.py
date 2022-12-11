kosong = []
batas = int(input("masukkan batas : "))
print()

while True :
    angka = int(input("masukkan angka : "))
    kosong.append(angka)
    if len(kosong) == batas:
        break

print()
print("angka : ", kosong)
print()

def maksimal():
    #mencari nilai tertinggi
    print("nilai paling tinggi dalam list : ", max(kosong))

def minimal():
    #mencari nilai terendah
    print("nilai paling rendah dalam list : ", min(kosong))

def semua():
    print("nilai paling tinggi dalam list : ", max(kosong))
    print("nilai paling rendah dalam list : ", min(kosong))

while True:
    print('''jenis pilihan
1. menampilkan nilai maksimal
2. menampilkan nilai minimal
3. menampilkan nilai maksimal dan menampilkan nilai minimal''')

    pilihan = input("masukkan pilihan : ")
    if pilihan == "1":
        maksimal()
        print()
    elif pilihan == "2":
        minimal()
        print()
    elif pilihan == "3":
        semua()
        print()

    stop = input("pilih y untuk lanjut : ")
    if stop == "y":
        break
        
