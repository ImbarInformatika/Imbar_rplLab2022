a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka pertama : "))

jumlah = a + b

print()
if jumlah % 2 == 0:
	print(f'''jumlah sebelum di tambah : {jumlah} setelah di jumlah : {jumlah+1}''')
	
elif jumlah % 2 != 0:
	print(f'''jumlah sebelum di tambah : {jumlah} setelah di jumlah : {jumlah+2}''')