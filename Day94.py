#Perpangkatan dengan perulangan for

bilangan = int(input("Masukkan bilangan : "))
print()
pangkat = int(input("Masukkan pangkat : "))
print()

hasil = bilangan

for i in range(pangkat - 1):
  hasil *= bilangan

print(f"Hasil dari {bilangan} pangkat {pangkat} adalah : ", hasil)