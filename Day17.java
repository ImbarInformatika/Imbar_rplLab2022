package rpl;
public class Day17 {
    public static void main(String[] args) {
        for (int angka=1; angka<9; angka++)
        {
            if (angka == 5)//ketika angka sama dengan lima maka, angka lima tidak akan di tampilkan dan akan menampilkan angka selanjutnya;
            {
                System.out.println("tidak dihitung");
                continue;
            }
            else if (angka == 7)//ketika angka sama dengan 7 maka program akan berhenti 
            {
                break;
            }
            System.out.println("Angka ke -"+angka);
        }
    }
}
