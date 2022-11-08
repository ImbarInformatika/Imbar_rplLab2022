package rpl;
public class Day16 {
    public static void main(String[] args) {
        for (int angka = 0; angka < 8; angka++)
        {
             if (angka == 5)
            {
                continue;
            }
            System.out.println("angka ke>" + angka);
        }
    }
}
