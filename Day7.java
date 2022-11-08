package rpl;

import java.util.Scanner;

public class Day7 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("masukkan nama Anda : ");
        String nama = input.nextLine();
        
        System.out.println();
        System.out.print("Masukkan Tahun lahir Anda : ");
        int tahun_lahir = input.nextInt();
        int usia = 2022 - tahun_lahir;
        System.out.println("Umur kamu : " + usia);
    }
}
