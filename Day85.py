print ("")
print ("MENGHITUNG SALDO DAN BUNGANYA")
print ("")
print ("")

tabungan = int(input("Masukkan jumlah tabungan : "))
lama = int(input("Masukkan jumlah lama menabung (bulan) : "))
 
if tabungan > 500000 or tabungan < 1000000:
	bunga = (tabungan * lama*3)/100
	
elif tabungan > 1000000 or tabungan < 2000000:
	bunga = (tabungan*lama *4)/100

elif tabungan > 2000000:
	bunga = (tabungan * lama*5)/100
	
else:
	bunga = 0

print()
print(f'''Setelah menabung selama {lama} bulan dengan tabungan perbulan Rp.{tabungan} maka total tabungan Rp. {tabungan*lama} maka anda mendapatkan bunga sebesar Rp. {bunga}''')
print()
print("total saldo anda adalah : Rp. ", tabungan * lama + bunga)	