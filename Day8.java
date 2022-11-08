package rpl;

import java.util.Scanner;

public class Day8 {
    public static void main(String[] args) {
        System.out.println("pilih operator anda");
        System.out.println("1. Penjumlahan");
        System.out.println("2. Perkalian");
        System.out.println("3. Pengurangan");
        System.out.println("4. Pembagian");
 
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan pilihan anda : ");
        int pilihan = input.nextInt();
        
        System.out.println();
        System.out.print("masukkan bilangan 1 : ");
        int bilangan1 = input.nextInt();
        System.out.print("masukkan bilangan 2 : ");
        int bilangan2 = input.nextInt();
        
        if (pilihan == 1){
            int hasil = bilangan1 + bilangan2;
            System.out.println("Hasil penjumlahan bilangan : "+hasil);
        }else if (pilihan == 2){
            int hasil = bilangan1 * bilangan2;
            System.out.println("Hasil perkalian bilangan : "+hasil);
        }else if (pilihan == 3){
            int hasil = bilangan1 - bilangan2;
            System.out.println("Hasil perngurangan bilangan : "+hasil);
        }else if (pilihan == 4){
            int hasil = bilangan1 / bilangan2;
            System.out.println("Hasil pembagian bilangan : "+hasil);
        }
    }
}
