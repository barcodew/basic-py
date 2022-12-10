import os

def fungsi(bil):
    if bil %2 == 0:
        print("Bilangan Yang Anda Masukkan Adalah Genap!")
    else:
        print("Bilangan Yang Anda Masukkan Adalah Ganjil!")


while True:

    bilangan = int(input("Masukkan Bilangan :"))
    fungsi(bilangan)
    njut = input("Ingin Melanjutkan Program? (y/n) :")
    os.system("cls")
    if njut == "n" or njut == "N":
        break
print("Program Selesai!, Semoga Harimu Suram.")
