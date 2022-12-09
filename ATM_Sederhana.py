
import os
saldo_bar = 100000000
def struk(anu,nominal):
    print(40*'=')
    print('='*15,'Tarik Tunai','='*15)
    print(40*'=')
    print('')
    print(f'Anda berhasil Melakukan Penarikan Sebesar Rp {nominal:,}'.replace(",","."))
    print('')
    print(f'\tSisa Saldo Anda {anu}'.replace(',',"."))
    print(40*'=')




while True:
    print("Selamat Datang Di Bank Apa?")
    print("="*14)
    print("""
1. Cek Saldo
2. Transfer
3. Setor Tunai
4. Tarik Tunai
5. Exit
    """)
    print("="*14)
    inputan = float(input("Masukkan Menu :"))

    if inputan == 1:
        print(f"Sisa Saldo Kamu Rp. {saldo_bar:,}".replace(",","."))
    elif inputan == 2:
            tf1= float(input("\nMasukkan Jumlah Transfer :"))
            if saldo_bar <=tf1:
                print("\nSaldo Anda Tidak Cukup!")
            else:
                sisa =  saldo_bar - tf1
                print(f"\nBerhasil Mentransfer Sejumlah Rp.{tf1:,}\nJadi Sisa Saldo Anda Rp {sisa:,}".replace(",","."))
    elif inputan == 3:
        setor = float(input("\nMasukkan Jumlah Setoran :"))
        hasil_setor = saldo_bar + setor
        print(f"\nAnda Berhasil Menyetor Uang Sebesar Rp . {setor:,}\nSaldo Saat Ini Rp. {hasil_setor}\n\n".replace(",","."))
    elif inputan == 4:
        os.system('cls')
        print(40*'=')
        print("="*12,"Pilih Nominal","="*13)
        print(40*'=')
        print('')
        print("1. 100.000\t\t4. 1.000.000")
        print("2. 300.000\t\t5. 1.500.000")
        print("3. 500.000\t\t6. 2.000.000")
        print('')
        print(40*'=')
        print('\tSilahkan Pilih Nominal')
        nominal = int(input('\t\t   '))
        if nominal == 1:
            uang = 100000
            trx = saldo_bar - uang
            struk(trx,uang)
        elif nominal == 2:
            uang = 300000
            trx = saldo_bar - uang
            struk(trx,uang)
        elif nominal == 3:
            uang == 500000
            trx = saldo_bar - uang
            struk(trx,uang)
        elif nominal == 4:
            uang == 1000000
            trx = saldo_bar - uang
            struk(trx,uang)
        elif nominal == 5:
            uang == 1500000
            trx = saldo_bar - uang
            struk(trx,uang)
        elif nominal == 6:
            uang == 2000000
            trx = saldo_bar - uang
            struk(trx,uang)
    elif inputan == 5:
        break

    gas = input("Lanjut Transaksi? (Y/n) : ")
    if gas == "y" or gas == "Y":
        dummy = 0
        os.system('cls')
    elif gas == 'n' or gas == 'N':
        break

    else:
        print("Pilih Menu Dengan Benar!")
print('Program Selesai , Have a Nice Day')
