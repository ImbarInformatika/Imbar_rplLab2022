package rpl;

import java.util.Scanner;

public class Day25 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan Nilai Anda : ");
        int nilai = input.nextInt();
        
        if (nilai == 100 && nilai >=85){
            System.out.println("Nilai Kamu Berpredikat A");
        }else if (nilai <= 84 && nilai >=75){
            System.out.println(" Nilai Kamu Berpredikat B");
        }else if (nilai <= 74 && nilai >=65){
            System.out.println("Nilai Kamu Berpredikat C");
        }else if (nilai <= 64 && nilai >=55){
            System.out.println("Nilai Kamu Berpredikat D");
        }else if (nilai <= 54 && nilai >=5){
            System.out.println("Nilai Kamu Berpredikat E");
        }else{
            System.out.println("Nilai Kamu Berpredikat T");
        }
    }
}
