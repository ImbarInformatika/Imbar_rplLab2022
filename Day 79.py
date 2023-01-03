def ulang():
	while True:
		angka = int(input("Masukkan angka : "))
		if angka % 2 == 0:
			ulang()
	
		else :
			stop()
		break
	
def stop():
	print("you and i, end")

angka = int(input("masukkan angka : "))
if angka % 2 == 0:
	ulang()
	
else :
	stop()