#menampilkan nilai yang habis dibagi 3 dengan perulangan

batas = int(input("Masukkan batas atas : "))

for i in range(1, batas, 2):
	if i % 3 == 0:
		print(i)