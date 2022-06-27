

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
    print("hasil dari", nilai1, ' - ', nilai2, "   :", hasil)
    print("")
    print("===============================================================================")
    print("")


def perkalian():
    print("============================= Program Perkalian 😂 ===============================")
    print("")
    nilai1 = int(input("masukan nilai pertama: "))
    nilai2 = int(input("masukan nilai kedua  : "))
    hasil = nilai1 * nilai2
    print("hasil dari", nilai1, ' x ', nilai2, "   :", hasil)
    print("")
    print("===============================================================================")
    print("")


def pembagian():
    print("============================= Program Pembangian 😁 ==============================")
    print("")
    nilai1 = int(input("masukan nilai pertama: "))
    nilai2 = int(input("masukan nilai kedua  : "))
    hasil = nilai1 / nilai2
    print("hasil dari", nilai1, ' : ', nilai2, "   :", hasil)
    print("")
    print("===============================================================================")
    print("")


def volumeBalok():
    print("============================= Program Volume Balok 😝 ============================")
    print("")
    panjang = int(input("masukan panjang\t\t: "))
    lebar = int(input("masukan lebar\t\t: "))
    tinggi = int(input("masukan tinggi\t\t: "))
    hasil = panjang*lebar*tinggi
    print("Volume Balok adalah\t:", hasil)
    print("===============================================================================")
    print("")


def luasSegitiga():
    print("============================= Program Luas Segitga 😃 ============================")
    print("")
    alas = float(input("masukan panjang\t\t: "))
    tinggi = float(input("masukan lebar\t\t: "))
    hasil = 1/2 * alas * tinggi
    print("Luas Segitiga adalah\t:", hasil)
    print("===============================================================================")
    print("")


def luasLingkaran():
    print("============================= Program Luas Lingkaran 😎 ===========================")
    print("")
    alas = float(input("masukan panjang\t\t: "))
    tinggi = float(input("masukan lebar\t\t: "))
    hasil = 1/2 * alas * tinggi
    print("Luas Segitiga adalah\t:", hasil)
    print("===============================================================================")
    print("")

# Testing Function
# penjumlahan()
# pengurangan()
# perkalian()
# pembagian()
# volumeBalok()
# luasSegitiga()
# luasLingkaran()

while True:
    print("============================= Program MtkSolution =============================")
    print("")
    print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Luas Balok\n6. Luas Segitiga\n7. Luas Lingkaran\n8. Luas Kubus\n\n0. keluar program")
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
    else :
        print("")
        print("Anda Telah Keluar dari program")
        break
