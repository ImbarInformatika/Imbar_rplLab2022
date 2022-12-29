class bangunruang():
    def luaspersegi():
        print("====== Luas Persegi ======")
        panjang = int(input("masukkan panjang : "))
        lebar = int(input("masukkan lebar : "))
        persegi = panjang * lebar
        print("luas persegi : ", persegi)
        bangunruang.berhenti()
        
        
    def luassegitiga():
        print("====== Luas Segitiga ======")
        alas = int(input("masukkan alas : "))
        tinggi = int(input("masukkan tinggi : "))
        luassegitiga = alas * tinggi / 2
        print("luas segitiga : ", luassegitiga)
        bangunruang.berhenti()
        
    def luaslingkaran():
        print("====== Luas Lingkaran ======")
        jari = int(input("masukkan jari jari : "))
        if jari % 7 == 0:
            phi = 22/7
        else :
            phi = 3.14
        luaslingkaran = phi * jari * jari
        print("luas lingkaran : ", luaslingkaran )
        bangunruang.berhenti()
    
    def berhenti():
        print()
    
class volume():
    def volumetabung():
        jari = int(input("masukkan jari jari : "))
        if jari % 7 == 0:
            phi = 22/7
        else :
            phi = 3.14
        tinggi = int(input("masukkan tinggi : "))
        volumelingkaran = phi * jari * jari * tinggi
        print("volume lingkaran : ", volumelingkaran)
        volume.berhenti()
        
    def volumebalok():
        panjang = int(input("masukkan panjang : "))
        lebar = int(input("masukkan lebar "))
        tinggi = int(input("masukkan tinggi "))
        volumebalok = panjang * lebar * tinggi
        print("volume balok ", volumebalok)
        volume.berhenti()
        
    def volumesegitiga():
        alas = int(input("masukkan alas : "))
        tinggi = int(input("masukkan tinggi : "))
        volumesegitiga = alas * tinggi / 2
        print("volume segitiga : ", volumesegitiga)
        volume.berhenti()
        
    def berhenti():
        print()
        
while True:
    print('''pilih yang akan di tampilkan
          1. bangun ruang
          2. volume
          3. keluar''')
    
    pilih = input("masukkan pilihan : ")
    if pilih == "1":
        while True:
            print('''pilih yang akan di tampilkan
              1. luas persegi
              2. luas segitiga
              3. luas lingkaran
              4. keluar''')
            plh = input("masukkan pilihan : ")
            if plh == "1":
                bangunruang.luaspersegi()
            elif plh == "2":
                bangunruang.luassegitiga()
            elif plh == "3":
                bangunruang.luaslingkaran()
            elif plh == "4":
                break
            else:
                print("periksa kembali inputan anda")
                
    elif pilih == "2":
        while True:
            print('''pilih yang akan di tampilkan
              1. volume lingkaran
              2. volumen balok
              3. volume persegi
              4. keluar''')
            plh = input("masukkan pilihan : ")
            if plh == "1":
                volume.volumetabung()
            elif plh == "2":
                volume.volumebalok()
            elif plh == "3":
                volume.volumesegitiga()
            elif plh == "4":
                break
            else:
                print("periksa kembali inputan Anda")
    else:
        break
