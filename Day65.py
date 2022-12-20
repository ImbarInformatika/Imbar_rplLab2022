brg = []

user = 0

while user != 7 :
  print('''
  1. menambahkan
  2. menghapus
  3. mengedit
  4. menampilkan 
  5. mencari barang
  6. mencari index
  7. keluar
  ''')

  user = int(input("masukkan operator anda : "))

  if user == 1 :
    while True :
      t = input("masukkan barang : ")
      brg.append(t)

      print("barang sekarang : ", brg)

      stop = input("ketik y untuk berhenti : ")
      if stop == 'y':
        break
    
  elif user == 2 :
    while True :
      t = int(input("masukkan index yang akan di hapus : "))

      if t >= len(brg):
        print("index tidak ditemukan")
      else : 
        print(brg.pop(t))

      print("barang sekarang : ", brg)

      stop = input("ketik y untuk berhenti : ")
      if stop == 'y':
        break

  elif user == 3 :
    while True:
      r = int(input("masukkan index yang akan di ganti : "))

      if r > len(brg):
        print("index tidak di temukan")
      else :
        brg[r] = input("masukkan barang pengganti : ")

      print("barang sekarang : ", brg)

      stop = input("ketik y untuk berhenti : ")
      if stop == 'y':
        break
  
  elif user == 4 :
    for i in range(len(brg)):
      print("barang sekarang", brg[i])
  
  elif user == 5 :
    cari = input("masukkan barang yang di cari :")

    if cari in brg:
      print("barang di temukan")

    else :
      print("barang tidak ditemukan")

  
  elif user == 6 :
    for i in range(len(brg)):
    	print(i[brg])
    cari1 = input("masukkan barang yang di cari : ")

    if cari1 in brg: 
      print(f"{cari1} ditemukan pada index ke- {brg.index(cari1)}")
    else :
      print("barang tidak ditemukan")
      
  else:
    print("periksa kembali")