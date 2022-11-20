package rpl;

import java.util.Scanner;

public class Day35 {
    public static void main(String[] args) {
        //menghitung luas dan keliling persegi panjang
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan Panjang : ");
        int panjang = input.nextInt();
        System.out.print("Masukkan Lebar : ");
        int lebar = input.nextInt();
        
        int luas = panjang * lebar;
        int keliling = 2 * (panjang + lebar);
        
        System.out.println("Luas Persegi Panjang : " + luas);
        System.out.println("Keliling Persegi Panjang : " + keliling);
    }
    
}
