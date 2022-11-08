package rpl;
public class Day6 {
    public static void main(String[] args) {
        int a, b, tambah, kurang, bagi, kali, modulus ;
        
        a = 5;
        b = 5;
        
        tambah = a + b;
        kurang = a - b;
        bagi = a / b;
        kali = a * b;
        modulus = a % b;
        
        System.out.println("Hasil Tambah : " + tambah);
        System.out.println("Hasil Kurang : " + kurang);
        System.out.println("Hasil Bagi : " + bagi);
        System.out.println("Hasil Kali : " + kali);
        System.out.println("Hasil Sisa Bagi : " + modulus);  
    }
}
