gaji = int(input("Masukkan Gaji : "))
kerjaan = input("Masukkan Pekerjaan : ").lower()

if gaji >= 3000000 or gaji < 300000:
	pajak = 3/100
	potongan = (gaji * 3)/100
	total_gaji = gaji - potongan
elif gaji >= 5000000:
	pajak = 5/100
	potongan = (gaji*5)/100
	total_gaji = gaji - potongan
	
else:
	pajak = 0/100
	potongan =(gaji*0)/100
	total_gaji = gaji - potongan
	
if kerjaan == "pns":
	pajakp = 5/100
	potonganp = (total_gaji * 5)/100
	total_potongan = potongan + potonganp
else:
	pajakp = 0/100
	potonganp = (total_gaji * 0)/100
	total_potongan = potongan + potonganp

print()	
print("===== Gaji Karyawan ======")
print("Gaji         : ", gaji)
print("Pekerjaan    : ", kerjaan)
print("Pajak        : ", pajak + pajakp, "%")
print("Potongan     : ", total_potongan)
print("Gaji Bersih  : ", gaji - total_potongan)