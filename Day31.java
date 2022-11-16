package rpl;
import java.util.Scanner;
public class Day31 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan nilai pertama : ");
        int pertama = input.nextInt();
        
        System.out.print("Masukkan nilai kedua : ");
        int kedua = input.nextInt();
        
        System.out.print("Masukkan nilai ketiga : ");
        int ketiga = input.nextInt();
        
        if (pertama <= kedua && pertama <= ketiga)
            System.out.println(pertama + " merupakan bilangan terkecil");
        else if (kedua <= pertama && kedua <= ketiga)
            System.out.println(kedua + " merupakan bilangan terkeci");
        else
            System.out.println(ketiga + " merupakan bilangan terkecil");
    }
    
}
