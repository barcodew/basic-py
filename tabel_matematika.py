# made with love by Barcodew ^__^

'''Tabel Matematika'''
import os
def tabel_menu():
    print("""
    1. Penjumlahan ( + )
    2. Pengurangan  ( - )
    3. Perkalian    ( X )
    4. Pembagian    ( / )
    5. Exit
    """)

def penjumlahan(angka):
    for i in range(1,11):
        print(f" {i} + {angka} = {i+angka}")
def pengurangan(angka):
    for i in range(1,11):
        print(f" {i} - {angka} = {i-angka}")
def perkalian(angka):
    for i in range(1,11):
        print(f" {i} X {angka} = {i*angka}")
def pembagian(angka):
    for i in range(1,11):
        print(f" {i} / {angka} = {(i/angka)}")



tabel_status = "y" # y = on

while  tabel_status.lower() == "y":
    tabel_menu()
    menu = int(input("Silahkan Pilih Menu   :")) 

    if menu == 1:
        angka = int(input("Mau Penjumlahan Berapa?  "))
        penjumlahan(angka)
        tabel_status = input("Lanjut ke operator lainnya? (Y/n)    :")
        os.system("cls")
    elif menu == 2:
        angka = int(input("Mau Pengurangan Berapa?  "))
        pengurangan(angka)
        tabel_status = input("Lanjut ke operator lainnya? (Y/n)    :")
        os.system("cls")
    elif menu == 3:
        angka = int(input("Mau Perkalian Berapa?  "))
        perkalian(angka)
        tabel_status = input("Lanjut ke operator lainnya? (Y/n)    :")
        os.system("cls")
    elif menu == 4:
        angka = int(input("Mau Pembagian Berapa?  "))
        pembagian(angka)
        tabel_status = input("Lanjut ke operator lainnya? (Y/n)    :")
        os.system("cls")
    elif menu == 5:
        break

print("Program Selesai, Semoga harimu Suram ^__^")
