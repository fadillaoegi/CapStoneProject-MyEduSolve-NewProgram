

def penjumlahan():
    print("============================= Program Penjumlahan 👌 =============================")
    print("")
    nilai1 = int(input("masukan nilai pertama : "))
    nilai2 = int(input("masukan nilai kedua   : "))
    hasil = nilai1 + nilai2
    print("hasil dari", nilai1, ' + ', nilai2, "   :", hasil)
    print("")
    print("===============================================================================")
    print("")


def pengurangan():
    print("============================= Program Pengurangan 😊 =============================")
    print("")
    nilai1 = int(input("masukan nilai pertama: "))
    nilai2 = int(input("masukan nilai kedua  : "))
    hasil = nilai1 - nilai2
    print("hasil dari", nilai1, ' - ', nilai2, "  :", hasil)
    print("")
    print("===============================================================================")
    print("")


def perkalian():
    print("============================= Program Perkalian 😂 ===============================")
    print("")
    nilai1 = int(input("masukan nilai pertama: "))
    nilai2 = int(input("masukan nilai kedua  : "))
    hasil = nilai1 * nilai2
    print("hasil dari", nilai1, ' x ', nilai2, "  :", hasil)
    print("")
    print("===============================================================================")
    print("")


def pembagian():
    print("============================= Program Pembangian 😁 ==============================")
    print("")
    nilai1 = int(input("masukan nilai pertama: "))
    nilai2 = int(input("masukan nilai kedua  : "))
    hasil = nilai1 / nilai2
    print("hasil dari", nilai1, ' : ', nilai2, "  :", hasil)
    print("")
    print("===============================================================================")
    print("")


def volumeBalok():
    print("============================= Program Volume Balok 😝 ============================")
    print("")
    panjang = int(input("masukan panjang\t\t: "))
    lebar = int(input("masukan lebar\t\t: "))
    tinggi = int(input("masukan tinggi\t\t: "))
    volumebalok = panjang*lebar*tinggi
    print("Volume Balok adalah\t:", volumebalok)
    print("===============================================================================")
    print("")


def luasBalok():
    print("============================= Program Volume Balok 😝 ============================")
    print("")
    panjang = int(input("masukan panjang\t\t: "))
    lebar = int(input("masukan lebar\t\t: "))
    tinggi = int(input("masukan tinggi\t\t: "))
    luasbalok = (2*panjang*lebar) * (2*panjang*tinggi) * (2*lebar*tinggi)
    print("Luas Balok adalah\t:", luasbalok)
    print("===============================================================================")
    print("")


def luasSegitiga():
    print("============================= Program Luas Segitga 😃 ============================")
    print("")
    alas = float(input("masukan alas\t\t: "))
    tinggi = float(input("masukan tinggi\t\t: "))
    luassegitiga = 0.5 * (alas * tinggi)
    print("Luas Segitiga adalah\t:", luassegitiga)
    print("===============================================================================")
    print("")


def luasBola():
    print("============================= Program Luas Bola 😎 ===========================")
    print("")
    r = float(input("masukan jari-jari\t: "))
    luasbola = 4 * 3.14 * (r**2)
    print("Luas Bola adalah\t:", luasbola)
    print("===============================================================================")
    print("")


def hitungKecepatan():
    print("============================= Program Hitung Kecepatan 😎 ===========================")
    print("")
    jarak = float(input("masukan jarak\t\t: "))
    waktu = float(input("masukan waktu\t\t: "))
    kecepatan = jarak * waktu
    print("Kecepatan adalah\t:", kecepatan)
    print("===============================================================================")
    print("")


def volumeKubus():
    print("============================= Program Hitung Kubus 😎 ===========================")
    print("")
    sisi = float(input("masukan sisi\t\t: "))
    hasil = sisi * sisi * sisi
    print("Luas Kubus adalah\t:", hasil)
    print("===============================================================================")
    print("")


while True:
    print("============================= Program MtkSolution =============================")
    print("")
    print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Volume Balok\n6. Luas Balok\n7. Luas Segitiga\n8. Luas Bola\n9. Luas Kubus\n10. Hitung Kecepatan\n\n0. keluar program")
    print("")
    inputProgram = int(input("Masukan nomer program : "))
    print("===============================================================================")

    if(inputProgram == 1) :
        penjumlahan()
    elif(inputProgram == 2) :
        pengurangan()
    elif(inputProgram == 3) :
        perkalian()
    elif(inputProgram == 4) :
        pembagian()
    elif(inputProgram == 5) :
        volumeBalok()
    elif(inputProgram == 6) :
        luasBalok()
    elif(inputProgram == 7) :
        luasSegitiga()
    elif(inputProgram == 8) :
        luasBola()
    elif(inputProgram == 9) :
        volumeKubus()
    elif(inputProgram == 10) :
        hitungKecepatan()
    else :
        print("")
        print("Anda Telah Keluar dari program")
        break


# @fdlml_ copyRight