package rpl;

import java.util.Scanner;

public class Day29 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Masukkan nilai A : ");
        int a = input.nextInt();
        
        System.out.print("Masukkan nilai B : ");
        int b = input.nextInt();
        
        if (a > b){
            int simpan = a;
            a = b;
            b = simpan;
        }
        System.out.println("NIlai a : " + a);
        System.out.println("NIlai b : " + b);
        
        
    }
    
}
