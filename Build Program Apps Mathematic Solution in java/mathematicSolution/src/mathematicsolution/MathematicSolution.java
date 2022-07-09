/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mathematicsolution;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author LENOVO
 */
public class MathematicSolution {

    
    public static void main(String[] args) throws Exception{
            BufferedReader input = new BufferedReader ( new InputStreamReader ( System.in ) );
        // TODO code application logic here
        int hasil;
        float hasil2;
        while (true) {          
            int choice;
            
            
            System.out.println("============================= Program MtkSolution =============================");
            System.out.println("");
            System.out.println("Silahkan_mau_beli_paket_apa_?");
            System.out.println("");
            System.out.println("1.)Penjumlahan");
            System.out.println("2.)Pengurangan");
            System.out.println("3.)Perkalian");
            System.out.println("4.)Pembagian");
            System.out.println("5.)Volume Balok");
            System.out.println("6.)Luas Balok");
            System.out.println("7.)Luas Segitiga");
            System.out.println("8.)Luas Bola");
            System.out.println("9.)Luas Kubus");
            System.out.println("10.)Hitung Kecepatan\n\n");
            System.out.println("0.)Keluar program");
            System.out.println("");
            System.out.print("Ketik_di_sini : ");
            choice = Integer.parseInt(input.readLine());
            
            if (choice == 1) {
                int pertama,kedua;
                System.out.println("============================= Program Penjumlahan 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai pertama: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai kedua: ");
                kedua = Integer.parseInt(input.readLine());
                hasil = pertama+kedua;
                System.out.println("hasil dari "+pertama+ '+'+kedua+" = " + hasil);
                
            } else if(choice == 2) {
                int pertama,kedua;
                System.out.println("============================= Program Pengurangan 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai pertama: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai kedua: ");
                kedua = Integer.parseInt(input.readLine());
                hasil = pertama-kedua;
                System.out.println("hasil dari "+pertama+ '-'+kedua+" = " + hasil);
            }else if(choice == 3) {
                int pertama,kedua;
                System.out.println("============================= Program Perkalian 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai pertama: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai kedua: ");
                kedua = Integer.parseInt(input.readLine());
                hasil = pertama*kedua;
                System.out.println("hasil dari "+pertama+ 'x'+kedua+" = " + hasil);
            }else if(choice == 4) {
                int pertama,kedua;
                System.out.println("============================= Program Pembagian 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai pertama: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai kedua: ");
                kedua = Integer.parseInt(input.readLine());
                hasil = pertama/kedua;
                System.out.println("hasil dari "+pertama+ ':'+kedua+" = " + hasil);
            }else if(choice == 5) {
                int pertama,kedua,ketiga;
                System.out.println("============================= Program Volume Balok 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai panjang\t\t: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai lebar\t\t: ");
                kedua = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai tinggi\t\t: ");
                ketiga = Integer.parseInt(input.readLine());
                hasil = pertama*kedua*ketiga;
                System.out.println("Volume Balok adalah "+hasil);
            }else if(choice == 6) {
                 int pertama,kedua,ketiga;
                System.out.println("============================= Program Luas Balok 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai panjang\t\t: ");
                pertama = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai lebar\t\t: ");
                kedua = Integer.parseInt(input.readLine());
                System.out.println("Masukan nilai tinggi\t\t: ");
                ketiga = Integer.parseInt(input.readLine());
                hasil = (2*pertama*kedua) * (2*pertama*ketiga) * (2*kedua*ketiga);
                System.out.println("Luas Balok adalah "+hasil);
            }else if(choice == 7) {
                float pertama,kedua,ketiga;
                System.out.println("============================= Program Luas Segitiga 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai alas\t\t: ");
                pertama = Float.parseFloat(input.readLine());
                System.out.println("Masukan nilai lebar\t\t: ");
                kedua = Float.parseFloat(input.readLine());
                hasil2 = (float) (0.5 * (pertama * kedua));
                System.out.println("Luas Segitiga adalah "+hasil2);
            }else if(choice == 8) {
                float pertama,kedua,ketiga;
                System.out.println("============================= Program Luas Bola👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai jari jari\t\t: ");
                pertama = Float.parseFloat(input.readLine());
                hasil2 = (float) (4 * 3.14 * (pertama*2) * (pertama*2));
                System.out.println("Luas Bola adalah "+hasil2);
            }else if(choice == 9) {
                float pertama,kedua,ketiga;
                System.out.println("============================= Program Luas Kubus👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai sisi\t\t: ");
                pertama = Float.parseFloat(input.readLine());
                hasil2 = pertama*pertama*pertama;
                System.out.println("Luas Kubus adalah "+hasil2);
                
            }else if(choice == 10) {
                float pertama,kedua,ketiga;
                System.out.println("============================= Program hitung kecepatan 👌 =============================");
                System.out.println("");
                System.out.println("Masukan nilai jarak\t\t: ");
                pertama = Float.parseFloat(input.readLine());
                System.out.println("Masukan nilai waktu\t\t: ");
                kedua = Float.parseFloat(input.readLine());
                hasil2 = pertama * kedua;
                System.out.println("Kecepatan nya adalah "+hasil2);
            } else{
                System.out.println("========================= Anda telah Keluar Program =========================");
                break;
            }
            
            
        }
        
        
    }
    
    
    void penjumlahan(){
        
        
    }
    
}
