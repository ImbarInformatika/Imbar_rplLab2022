uang = input("Masukkan uang : ")
jumlah = len(uang)

print()
if jumlah == 4:
	print("ribuan")
	
elif jumlah == 5:
	print("puluhan ribu")
	
elif jumlah == 6:
	print("ratusan ribu")
	
elif jumlah == 7:
	print("jutaan")
	
elif jumlah == 8:
	print("puluhan juta")
	
else:
	print("tidak terdefenisi")
