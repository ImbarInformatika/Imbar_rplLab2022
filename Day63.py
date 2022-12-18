
def persegi():
    #mencari luas persegi
    print("<====> Mencari Luas PERSEGI <====>")
    sisi = int(input("MASUKKAN SISI PERSEGI : "))
    luas_persegi = sisi * sisi
    print("luas persegi adalah : ", luas_persegi, "cm")


def lingkaran():
    #mencari luas lingkaran
    print("<====> Mencari Luas LINGKARAN <====>")
    phi = 3.14
    r = int(input("MASUKKAN JARI JARI LINGKARAN : "))
    luas_lingkaran = phi*r*r
    print("luas lingkaran adalah : ", luas_lingkaran, "cm")

def segitiga():
    #mencari luas segitiga
    print("<====> Mencari Luas SEGITIGA <====>")
    alas = int(input("MASUKKAN ALAS SEGITIGA : "))
    tinggi = int(input("MASUKKAN TINGGI SEGITIGA : "))
    luas_segitiga = 1/2*alas*tinggi
    print("luas segitiga : ",luas_segitiga)

while True:
    print()
    print('''PILIH LAH BANGUN DATAR YANG AKAN DI TAMPILKAN LUASNYA
        1. persegi
        2. lingkaran
        3. segitiga''')
    print()
    pilihan = input("MASUKKAN PILIHAN ANDA : ")
    print()
    if pilihan == "1":
        persegi()

    elif pilihan == "2":
        lingkaran()

    elif pilihan == "3":
        segitiga()
    else:
        print()
        print("SILAHKAN PERIKSA KEMBALI INPUTAN ANDA")

    print()
    stop = input("KETIK y UNTUK BERHENTI : ")
    if stop == "y":
        print("TERIMAH KASIH")
        break