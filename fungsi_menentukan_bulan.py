import os
def bulanbulan(bulanan):
    namabulan = ["Januari","Februari","Maret","April","Mei","Juni","juli",
    "Agustus","September","Oktober","November","Desember"]

    return namabulan[bulanan -1]

while True:
    nilai = int(input("Masukkan Bulan Ke berapa?    :"))
    if nilai <=0 or nilai >= 13:
        print("Masukkan Angka Yang Benar!")
    else:
        print(bulanbulan(nilai))

    njut = input("Lanjut ga? Y/n")
    os.system('cls')
    if njut == "n" or njut =="N":
        break
