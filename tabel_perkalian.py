import os

status = "y"
while status.lower() == "y":
    os.system("cls")
    perkalian = int(input("Mau Perkalian Berapa? :"))
    if perkalian >0:
        os.system('cls')
        print("="*25)
        print(f"Tabel Perkalian {perkalian}")
        print("="*25)
        for i in range(1,11):
            print(perkalian,"x", i, "=", perkalian*i)
        print("="*25)
        status = input("\n\nIngin Melanjutkan Program? (Y/n) : ")
    else:
        os.system('cls')
        print("Jangan Masukkan Angka Negatif tolol")
        status = input("\n\nIngin Melanjutkan Program? (Y/n) : ")

print("Program Selesai! Semoga Harimu Suram !")
