nama = []
jumlah = int(input("MASUKKAN BATAS : "))
        
while True:
    if len(nama) == jumlah:
        break
    print()
    teman = input("MASUKKAN NAMA : ")
    keberapa = int(input("Masukkan Index : "))
    nama.insert(keberapa, teman)
    print(nama)
    print()
