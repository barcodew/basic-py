import random
import time
import os
game_start = True

coba = 0
while game_start == True:
    print("")
    print("="*40)
    print("Selamat Datang Di Game Tebak Angka ^__^")
    print("="*40)
    print("")
    print("""
    1. Start Game
    2. Exit
    """)
    print("")
    start = int(input("Pilih Menu :"))
    if start == 1:
            nama = input("Masukkan Nama Kamu :")
            os.system('cls')
            print(" ")
            print(f"Halo {nama} Selamat Datang Di Game Tebak Angka XcoBar! 1.0 ")
            print(" ")
            nebak = True
            tebak = random.randint(1,30)
            while nebak == True:
                print(f"Ayo Coba Tebak Angka ini XX !")
                angka = int(input("\t\t"))
                if angka < tebak:
                    os.system('cls')
                    print("Tebakan Mu Salah! Coba Lagi! Angka yang Lebih Besar Dari Ini!")
                    coba +=1
                    time.sleep(2)
                elif angka > tebak:
                    os.system('cls')
                    print("Tebakan Mu Salah! Coba Lagi! Angka yang Lebih Kecil Dari Ini!")
                    coba +=1
                    time.sleep(2)
                elif angka == tebak:
                    coba +=1
                    print(f"Selamat Tebakanmu Benar!!! Dalam {coba} Kali Percobaan Kamu Sangat Hebat! {nama}")
                    time.sleep(2)
                    ingin = input("Ingin Melanjutkan permainan? (Y/n) : ")
                    if ingin == "y" or ingin == "Y":
                        nebak == True
                        tebak = random.randint(1,30)
                        coba = 0
                        os.system('cls')
                    elif ingin == 'n' or ingin == "N":
                        nebak == False
                        game_start == False
                        os.system('cls')
                        break
    elif start == 2:
        game_start = False
        break
print("Program Selesai! , Have a Nice Day!")
