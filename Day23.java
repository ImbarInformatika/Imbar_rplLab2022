package rpl;

import java.util.Scanner;

public class Day23 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        String kode_pasien = "PS0003";
        String status_pasien;
        int biaya_pendaftaran;
        if (kode_pasien == "PS0001") {
            status_pasien = "Pasien Baru";
            biaya_pendaftaran = 500000;
        } else if (kode_pasien == "PS0002") {
            status_pasien = "Pasien Lama";
            biaya_pendaftaran = 400000;
        } else if (kode_pasien == "PS0003") {
            status_pasien = "Pasien BPJS";
            biaya_pendaftaran = 300000;
        } else if (kode_pasien == "PS0004") {
            status_pasien = "Pasien Akses";
            biaya_pendaftaran = 200000;
        } else {
            status_pasien = "kosong";
            biaya_pendaftaran = 0;
        }

        
        int kode_kamar = 4444;
        String nama_kamar;
        int biaya_kamar;
        if (kode_kamar == 1111) {
            nama_kamar = "Kamar Melati";
            biaya_kamar = 1000000;
        } else if (kode_kamar == 2222) {
            nama_kamar = "Kamar Mawar";
            biaya_kamar = 2000000;
        } else if (kode_kamar == 3333) {
            nama_kamar = "Kamar Dahlia";
            biaya_kamar = 3000000;
        } else if (kode_kamar == 4444) {
            nama_kamar = "Kamar Anggrek";
            biaya_kamar = 4000000;
        } else {
            nama_kamar = "kosong";
            biaya_kamar = 0;
        }

        
        String kode_dokter = "DK003";
        String nama_dokter;
        int biaya_pemeriksaan;
        if (kode_dokter == "DK001") {
            nama_dokter = "DR Andi";
            biaya_pemeriksaan = 500000;
        } else if (kode_dokter == "DK002") {
            nama_dokter = "DR Joko";
            biaya_pemeriksaan = 400000;
        } else if (kode_dokter == "DK003") {
            nama_dokter = "DR Karni";
            biaya_pemeriksaan = 300000;
        } else if (kode_dokter == "DK004") {
            nama_dokter = "DR Amin";
            biaya_pemeriksaan = 200000;
        } else if (kode_dokter == "DK005") {
            nama_dokter = "DR.l Udin";
            biaya_pemeriksaan = 100000;
        } else {
            nama_dokter = "kosong";
            biaya_pemeriksaan = 0;
        }
            
        
        int lama_menginap = 5;
        int diskon;
        if (lama_menginap > 10) {
            diskon = 50;
        } else if (lama_menginap > 8) {
            diskon = 40;
        } else if (lama_menginap > 6) {
            diskon = 30;
        } else if (lama_menginap > 4) {
            diskon = 20;
        } else if (lama_menginap > 1) {
            diskon = 10;
        } else {
            diskon = 0;
        }
        
        int potongan = biaya_kamar * diskon / 100;
        int totalbayar = (biaya_pendaftaran + biaya_kamar + biaya_pemeriksaan) - potongan;

        System.out.println("<========> STRUK PEMBAYARAN PASIEN RUMAH SAKIT <========>");
        System.out.println("BIAYA PENDAFTARAN   : " + biaya_pendaftaran);
        System.out.println("NAMA KAMAR          : " + nama_kamar);
        System.out.println("BIAYA KAMAR         : " + biaya_kamar);
        System.out.println("NAMA DOKTER         : " + nama_dokter);
        System.out.println("BIAYA PEMERIKSAAN   : " + biaya_pemeriksaan);
        System.out.println("POTONGAN PERSEN     : " + diskon + "%");
        System.out.println("POTONGAN BIAYA      : " + potongan);
        System.out.println("TOTAL PEMBAYARAN    : " + totalbayar);

    }
    
}
