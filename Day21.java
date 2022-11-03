package rpl;
import java.util.Scanner;
public class Day21 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String teman[] = {"imbar", "amri", "sayyid", "ikbal", "sofyan"};
        
        System.out.print("Masukkan index : ");
        int index = input.nextInt();
        if (index > (teman).length)
            System.out.println(index +" tidak ditemukan dalam array");
        else
            System.out.println("index ke-"+ index + " ditemukan pada " + teman[index]);
    }
}
