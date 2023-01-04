#menentukan berapa buah yang tinggal

keranjang1 = 0
keranjang2 = 10
keranjang3 = 5

#keranjang 3 di kasi tetangga
#berapakah totol buah yang di berikan ke tetangga

sebelum_dikasitetangga = keranjang1 + keranjang2 + keranjang3

total_yangdikasitetangga = (keranjang1 + keranjang2) - keranjang3

print("sebelum dikasi tetangga : ", sebelum_dikasitetangga, "buah")
print("total yang di kasi tetangga : ", total_yangdikasitetangga, "buah")
