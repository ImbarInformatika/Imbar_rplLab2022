package rpl;

import java.util.Scanner;

public class Day12 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan Angka Anda : ");
        int angka = input.nextInt();
        
        if (angka % 2 ==0)
            System.out.println("Angka : " + angka + " adalah bilangan genap");
       else
            System.out.println("angka : " + angka + " adalag bilangan ganjil");
    }
    }
