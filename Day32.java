package rpl;
public class Day32 {
    public static void main(String[] args) {
        for (var awal = 1; awal < 17; awal++){
	if (awal == 5 || awal == 14){
            System.out.println("pertemuan ke " + awal + " diadakan kuis");
	}else if(awal == 8 || awal == 16){
	    System.out.println("pertemuan ke " + awal + " diadakan ujian");
	}else if(awal < 8){
            System.out.println("pertemuan ke " + awal + " telah selesai");
	}else{
        System.out.println("pertemuan ke " + awal + " belum selesai");
	}
        }
    } 
}
