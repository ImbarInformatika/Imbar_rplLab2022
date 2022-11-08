package rpl;

import java.util.Scanner;

public class Day11 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan nama Kamu : ");
        String nama = input.nextLine();
        
        switch (nama)
            {
                case "imbar" :
                    System.out.println(nama+ " merupakan mahasiswa informatika semester tiga");
                case "edwin" :
                    System.out.println(nama+ " merupakan mahasiswa informatika semester tiga");
                default:
                    System.out.println(nama+ " bukan merupakan mahasiswa informatika semester tiga");
                    
        }
    }
    
}
