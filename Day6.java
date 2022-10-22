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
        
        System.out.println("Hasil tambah : " + tambah);
        System.out.println("Hasil kurang : " + kurang);
        System.out.println("Hasil bagi : " + bagi);
        System.out.println("Hasil kali : " + kali);
        System.out.println("Hasil sisa bagi : " + modulus);  
    }
}
