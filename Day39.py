saldo = 2000000

print("<=====> SELAMAT DATANG DI ATM SEDERHANA KAMI <=====>")
print()
def satu():
    penarikan = int(input("MASUKKAN JUMLAH PENARIKAN : "))
    global saldo
    if penarikan > saldo:
        print("SALDO ANDA TIDAK CUKUP")
    else:
        if penarikan > 200000:
            admin = 5000;
        else:
            admin = 0;
        saldo = saldo - penarikan - admin;
        print("<====> INFORMASI PENARIKAN <====>")
        print("JUMLAH PENARIKAN : ", penarikan)
        print("BIAYA ADMIN      : ", admin)

def dua():
    global saldo
    setoran = int(input("MASUKKAN JUMLAH SETORAN : "))
    if setoran > 200000:
        admin = 5000;
    else:
        admin = 0;
    saldo = (saldo + setoran) - admin;
    print("<====> INFORMASI SETORAN <====>")
    print("JUMLAH SETORAN : ", setoran)
    print("BIAYA ADMIN    : ", admin)

def tiga():
    global saldo
    rektr = int(input("MASUKKAN NOMOR REKENING TUJUAN : "))
    pengiriman = int(input("MASUKKAN JUMLAH PENGIRIMAN : "))
    if pengiriman > saldo:
        print("SALDO ANDA TIDAK CUKUP")
    else:
        if pengiriman > 200000:
            admin = 5000;
        else:
            admin = 0;

        saldo = saldo - pengiriman - admin;
        print("<====> INFORMASI PENGIRIMAN <====>")
        print("JUMLAH PENGIRIMAN : ", pengiriman)
        print("REKENING TUJUAN  : ", rektr)
        print("BIAYA ADMIN      : ", admin)

def empat():
    print("SALDO ANDA SEKARANG : ", saldo)


while True:
    pin = int(input("SILAHKAN MASUKKAN PIN ANDA : "));
    print()
    if pin == 12345:
        print('''MENU ATM SEDERHANA
1. PENARIKAN
2. SETORAN
3. PENGIRIMAN
4. CEK SALDO''')
        print()        
        pilihan = input("SILAHKAN PILIH MENU  ANDA : ")
        print() 
        if pilihan == "1":
            satu()
        elif pilihan == "2":
            dua()
                
        elif pilihan == "3":
            tiga()
                
        elif pilihan == "4":
           empat()

        else:
            print("PERIKSA KEMBALI PILIHAN MENU ANDA")
    else:
        print("SILAHKAN PERIKSA KEMBALI PIN ANDA")

    print()
    tl = input("TEKAN y UNTUK MELANJUTKAN TRANSAKSI : ")
    print()
    if tl == "y":
        print();
    else:
        print("TERIMAH KASIH")
        print("SELAMAT DATANG KEMBALI")
        break
        
