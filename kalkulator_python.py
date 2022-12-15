#made with love by barcodew ^__^

import os
import time
import sys


def tambah(a,b):
    hasil = a+b
    return hasil
def kurang(a,b):
    hasil = a-b
    return hasil
def kali(a,b):
    hasil = a*b
    return hasil
def bagi(a,b):
    hasil = a/b
    return hasil
def pangkat(a,b):
    hasil = a**b
    return hasil
def loadnjing():
    os.system('cls')
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.05)
        sys.stdout.write("\rLoading : " + animation[i % len(animation)])
        sys.stdout.flush()

def tittle():
    print("="*60)
    print(" ")
    print(f"{'Selamat Datang Di Kalkulator Sederhana':^40}")
    print(" ")
    print("="*60)
    print("""
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Pangkat
    6. Exit
     """)
    print(" ")
    print("="*60)
    print(" ")

kalku_stats = "y"

while kalku_stats == "y" or kalku_stats == "Y":

    tittle()
    maungapain = input('Silahkan Pilih Menu : ')
    angka_pertama = int(input("Masukkan Angka Pertama  :"))
    angka_kedua = int(input("Masukkan Angka Kedua  :"))

    if maungapain == "1":
        hasil = tambah(angka_pertama,angka_kedua)
        loadnjing()
        time.sleep(1)
        os.system('cls')  
        print(f"\n\n\t\tHasil Dari Penjumlahan {angka_pertama} + {angka_kedua} = {hasil}")
        kalku_stats = input("\n\nLanjut ? (Y/n)  :")
        os.system('cls')  
    elif maungapain == "2":
        hasil = kurang(angka_pertama,angka_kedua)
        loadnjing()
        time.sleep(1)
        os.system('cls')  
        print(f"\n\n\t\tHasil Dari Pengurangan {angka_pertama} - {angka_kedua} = {hasil}")
        kalku_stats = input("\n\nLanjut ? (Y/n)  :")
        os.system('cls')  
    elif maungapain == "3":
        hasil = kali(angka_pertama,angka_kedua)
        loadnjing()
        time.sleep(1)
        os.system('cls')  
        print(f"\n\n\t\tHasil Dari Perkalian {angka_pertama} X {angka_kedua} = {hasil}")
        kalku_stats = input("\n\nLanjut ? (Y/n)  :")
        os.system('cls')  
    elif maungapain == "4":
        hasil = bagi(angka_pertama,angka_kedua)
        loadnjing()
        time.sleep(1)
        os.system('cls')  
        print(f"\n\n\t\tHasil Dari Pembagian {angka_pertama} / {angka_kedua} = {hasil}")
        kalku_stats = input("\n\nLanjut ? (Y/n)  :")
        os.system('cls')  
    elif maungapain == "5":
        hasil = pangkat(angka_pertama,angka_kedua)
        loadnjing()
        time.sleep(1)
        os.system('cls')  
        print(f"\n\n\t\tPangkat {angka_kedua} Dari {angka_pertama} Adalah  = {hasil}")
        kalku_stats = input("\n\nLanjut ? (Y/n)  :")
        os.system('cls')  
    elif maungapain == 6:
        kalku_stats == "Turu"

    else:
        os.system('cls')
        print("Pilih Menu Dengan Benar!")

print("Program Selesai ! , Have a Nice Day ^__^")
        
