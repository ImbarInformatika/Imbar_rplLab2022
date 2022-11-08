package rpl;

import java.util.Scanner;

public class Day9 {
    public static void main(String[] args) {
        int gaji = 1000000;
        int gaji_lembur = 100000;
        int pajak = 5/100; //5 persen
        Scanner input = new Scanner (System.in);
        System.out.print("Hari lembur : ");
        int hari_lembur = input.nextInt();
        
        int gaji_bersih = gaji + (gaji_lembur * hari_lembur);
        System.out.println("Gaji bersih : "+ gaji_bersih);
        
        int total_pajak = gaji * 5/100;
        System.out.println("pajak total : "+ total_pajak);
        
        int gaji_total = gaji_bersih - total_pajak;
        System.out.println("gaji total : "+ gaji_total);
    }
}
