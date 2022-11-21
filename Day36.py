saldo = 2000000;

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
            penarikan = int(input("MASUKKAN JUMLAH PENARIKAN : "))
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
                
        elif pilihan == "2":
            setoran = int(input("MASUKKAN JUMLAH SETORAN : "))
            if setoran > 200000:
                admin = 5000;
            else:
                admin = 0;
            saldo = (saldo + setoran) - admin;
            print("<====> INFORMASI SETORAN <====>")
            print("JUMLAH SETORAN : ", setoran)
            print("BIAYA ADMIN    : ", admin)
            

        elif pilihan == "3":
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

        elif pilihan == "4":
            print("SALDO ANDA SEKARANG : ", saldo)

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
        
