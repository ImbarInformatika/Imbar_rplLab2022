package rpl;

import java.util.Scanner;

public class Day24 {
    public static void main(String[] args) {
        System.out.println("MENU WARUNG MAKAN SEDERHANA");
        System.out.println("<====> MENU NASI <====>");
        System.out.println("<=> 1. NASI KUNING");
        System.out.println("<=> 2. NASI PUTIH");
        System.out.println("<=> 3. NASI GORENG");
        System.out.println("<=> 4. NASI CAMPUR");

        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan Makanan Pilihanmu : ");
        int makanan = input.nextInt();
        System.out.print("Masukkan jumlah pesanan : ");
        int jumlah_pesanan = input.nextInt();
        
        int hargamakan = 0;
        String makan;
            
        if (makanan == 1){
            hargamakan = 10000;
            makan = "NASI KUNING";
        } else if(makanan == 2){
            hargamakan = 12000;
            makan = "NASI PUTIH";
        } else if(makanan == 3){
            hargamakan = 15000;
            makan = "NASI GORENG";
        }else if(makanan == 4){
            hargamakan = 20000;
            makan = "NASI CAMPUR";
        }
        int harga_makan = hargamakan * jumlah_pesanan;
        
        System.out.println("MENU WARUNG MAKAN SEDERHANA");
        System.out.println("<====> MENU AIR <====>");
        System.out.println("<=> 1. AQUA");
        System.out.println("<=> 2. LE MINARALE");
        System.out.println("<=> 3. TEH KOTAK");
        System.out.println("<=> 4. ES TEH MANIS");

        System.out.println();
        System.out.print("Masukkan Makanan Pilihanmu : ");
        int minuman = input.nextInt();
        System.out.print("Masukkan jumlah pesanan : ");
        int jumlahm = input.nextInt();
        
        int hargaminum = 0;
        String minum;
            
        if (minuman == 1){
            hargaminum = 5000;
            minum = "AQUA";
        } else if(minuman == 2){
            hargaminum = 9000;
            minum = "LE MINERALE";
        } else if(minuman == 3){
            hargaminum = 10000;
            minum = "TEH KOTAK";
        }else if(makanan == 4){
            hargaminum = 7000;
            minum = "ES TEH MENIS";
        }
        
        int harga_minum = hargaminum * jumlahm;
        
        int total_bayar = harga_makan + harga_minum;
        
        System.out.println();
        System.out.println("<========> STRUK PEMBAYARAN <========>");
        System.out.println("HARGA NASI          : " + harga_makan);
        System.out.println("HARGA MINUMAN       : " + harga_minum);
        System.out.println("TOTAL PEMBAYARAN    : " + total_bayar);
    }
}
