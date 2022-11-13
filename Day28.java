package rpl;

import java.util.Scanner;

public class Day28 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Menu Rumah Makan Sederhana");
        System.out.println("1. Nasi Putih");
        System.out.println("2. Nasi Kuning");
        System.out.println("3. Nasi Goreng");
        System.out.println("4. Nasi Campur");
        
        System.out.println();
        System.out.println("PETUNJUK PEMESANAN");
        System.out.println("JIKA ANDA INGIN MEMILIH NASI PUTIH KETIKKAN 1 ATAU 11");
        System.out.println("JIKA ANDA INGIN MEMILIH NASI KUNING KETIKKAN 2 ATAU 22");
        System.out.println("JIKA ANDA INGIN MEMILIH NASI GORENG KETIKKAN 3 ATAU 33");
        System.out.println("JIKA ANDA INGIN MEMILIH NASI CAMPUR KETIKKAN 4 ATAU 44");
        
        System.out.println();
        System.out.print("Masukkan Pesanan Anda : ");
        int pilihan_nasi = input.nextInt();
        System.out.print("Masukkan Jumlah Pesanan Anda : ");
        int jumlah = input.nextInt();
        
        String makanan_ku;
        int harga_nasi;
        if (pilihan_nasi == 1 || pilihan_nasi == 11) {
            makanan_ku = "Nasi Putih";
            harga_nasi = 9000;
        } else if (pilihan_nasi == 2 || pilihan_nasi == 22) {
            makanan_ku = "Nasi Kuning";
            harga_nasi = 12000;
        } else if (pilihan_nasi == 3 || pilihan_nasi == 33) {
            makanan_ku = "Nasi Goreng";
            harga_nasi = 15000;
        } else if (pilihan_nasi == 4 || pilihan_nasi == 44) {
            makanan_ku = "Nasi Campur";
            harga_nasi = 20000;
        } else{
            makanan_ku = "kosong";
            harga_nasi = 0;
        }

        System.out.println();
        int totalbayar = harga_nasi * jumlah;

        System.out.println("<========> STRUK PEMBAYARAN RUMAH MAKAN SEDERHANA <========>");
        System.out.println("PESANAN           : " + makanan_ku);
        System.out.println("HARGA NASI        : " + harga_nasi);
        System.out.println("JUMLAH PESAN      : " + jumlah);
        System.out.println("TOTAL PEMBAYARAN  : " + totalbayar);
    }
}
