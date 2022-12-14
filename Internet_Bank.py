import os
import time
import random
import string
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep



users_data = [
    {
        "id": 101,
        "users":"Guest_2",
        "pin":"666666",
        "name":"name",
        "balance":100,
        "rekening":123321
    },
    {
        "id":120,
        "users":"XcoBar",
        "pin":"123123",
        "name":"Achmad Ali Akbar",
        "balance":99999999999991,
        "rekening":123333
    },
    {
        "id":123,
        "users":"guest",
        "pin":"111111",
        "name":"Guest Account",
        "balance":10000,
        "rekening":123456
    }
]

def sapa(word):
    for i in word:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

def title():
    print("="*60)
    print(f"{'================== Bank Krupt Mobile Bank ==================':^60}")
    print("="*60,"\n")

def menu():
    print(f"{'1. Login':<40}\n{'2. Register':<40}\n{'3. Exit':<40}")
    print("="*60,"")
    print("="*60,"\n")

def menu_user():
    print("="*60)
    print(f"{'================== Bank Krupt Mobile Bank ==================':^60}")
    print("="*60)
    print(f" {'Hai Selamat Datang':<40}{cek_data['name']:<40}")
    print("="*60,"\n")
    print(f"1. Transfer\n2. Cek Saldo\n3. Setor Tunai\n4. Tarik Tunai\n5. Info Pengguna\n6. Log Out\n")
    print("="*60,"\n")
    
class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


def login_func(user,pin):
    for login in users_data:
        if login['users'] == user and login['pin'] == pin:
            return login
    return False
def verif_rek():
    status = "used"
    while status == "used":
        newrek = random.randint(99999999,9999999999)
        for rek in range(len(users_data)):
            if users_data[rek]['rekening'] != newrek:
                status = 'success'
                return int(newrek)
            else:
                status = "used"
def random_id():
    kepake = 'y'
    while kepake == 'y':
        new_id = random.randint(1,99999)
        for id in range(len(users_data)):
            if users_data[id]['id'] != new_id:
                kepake = 'g'
                return int(new_id)
            else:
                kepake = 'y'
def auth_id(auth_id):
    for id in range(len(users_data)):
        if str(users_data[id]['id']) == str(auth_id):
            return int(id)
    return -1

def auth_username(orang):
    for user in range(len(users_data)):
        if str(users_data[user]['users']) == str(orang) :
            return str(user)
    return -1
def auth_rek(rekeng):
    for rek in range(len(users_data)):
        if str(users_data[rek]['rekening']) ==  str(rekeng) :
            return int(rek)
    return -1
def verif_user(verif_users):
    for i in users_data:
        if i['users'] == verif_users:
            return True
    return verif_users
def register():
    status_regist = "Fail"
    while status_regist == "Fail": 
        os.system('cls')
        print(60*"=")
        print(f"{'Buka Rekening Baru':^60}")
        print(60*"=")
        nama_user = input("Masukkan Nama Lengkap :")
        new_user = input("Masukkan Username :")
        new_pin = input("Masukkan Pin Baru Min 6 (Angka) :")
        auth_new_pin = input("Masukkan Kembali Pin Min 6 (Angka) :")
        new_rek = verif_rek()
        new_id = random_id()
        cek_user = verif_user(new_user)
        print(60*"-")
        next_setep = input("Apakah Data Sudah Benar (Y/n) : ")
        os.system('cls')
        print('\033[92m')
        if __name__ == "__main__":
            with Loader("Mendaftarkan Akun ..."):
                for i in range(10):
                    sleep(0.25)
        print(60*"=",'\033[0m')
        os.system('cls')
        if next_setep == 'y' or next_setep == 'Y':
            if cek_user == True:
                print("-"*60)
                print("\n")
                print(f"USERNAME TELAH DIGUNAKAN !")
                print("\n")
                print("-"*60)
                time.sleep(5)
                status_regist = "Fail"
            elif len(new_pin) < 6 and len(auth_new_pin) < 6 :
                print("-"*60)
                print("\n")
                print(f"Mohon Masukkan 6 Digit PIN !")
                print("\n")
                print("-"*60)
                time.sleep(5)
                status_regist = "Fail"
            elif new_pin != auth_new_pin :
                print("-"*60)
                print("\n")
                print(f"Pin Yang Anda Masukkan Tidak Cocok! Silahkan Cek Kembali!")
                print("\n")
                print("-"*60)
                time.sleep(5)
                status_regist = "Fail"
            else:
                inputs_new_user = dict(id = new_id,users = new_user, pin = new_pin, rekening = new_rek,balance = 0,name = nama_user)
                users_data.append(inputs_new_user)
                print('\033[92m')
                print(60*'=')
                print("")
                print("\t\tPENDAFTARAN BERHASIL")
                print("")
                print("\t\tSILAHKAN LOGIN")
                print("")
                print(60*'=','\033[0m')
                time.sleep(6)
                os.system('cls')
                print('\033[92m')
                if __name__ == "__main__":
                    with Loader("Mengalihkan Menu! ..."):
                        for i in range(10):
                            sleep(0.25)
                print(60*"=",'\033[0m')
                status_regist = "success"

def transfer(balance,rekeningnya):
    login_user = auth_id(authid)
    target = auth_rek(rekeningnya)
    if login_user >=0:
        if users_data[login_user]['balance'] > int(balance):
            users_data[login_user]['balance'] = users_data[login_user]['balance'] - int(balance)
            users_data[target]['balance'] = users_data[target]['balance']  + int(balance)
            if __name__ == "__main__":
                with Loader("Transaksi Sedang Diproses..."):
                    for i in range(10):
                        sleep(0.25)
            print(60*"=",'\033[0m')
            os.system('cls')
            os.system('cls')
            print('\033[92m')
            print(60*"=")
            print("\t\t      Transaksi Berhasil".upper())
            print('')
            print(f"  Anda Berhasil Mengirim Rp {int(balance):,} ke Rekening {str(users_data[target]['rekening'])} A/N {str(users_data[target]['name'])}".replace(",","."))
            print('')
            print(60*"=","\033[0m")
            time.sleep(3)
        else:
            os.system('cls')
            print('\033[31m')
            if __name__ == "__main__":
                with Loader("Transaksi Gagal! Saldomu Gacukup!..."):
                    for i in range(10):
                        sleep(0.15)
            print(60*"=",'\033[0m')
            os.system('cls')
            print('\033[31m')
            print(60*"=")
            print('')
            print("\t\t   Saldo Anda Tidak Mencukupi")
            print('')
            print(f"\t\tSaldo Anda Saat ini Rp. {users_data[login_user]['balance']}")
            print(60*"=")
            print('\033[0m')

def cek_saldo():
    laujin = auth_id(authid)
    if laujin >=0:
        os.system('cls')
        print('\033[92m')
        if __name__ == "__main__":
            with Loader("Sabar Ngab ..."):
                for i in range(10):
                    sleep(0.25)
        print(60*"=",'\033[0m')
        os.system('cls')
        os.system('cls')
        print(60*"=")
        print('')
        print(f"\t\tSisa Saldo Anda Rp {users_data[laujin]['balance']:,}      ".replace(",","."))
        print('')
        print(60*"=")
def setoran(nominal):
    laujin = auth_id(authid)
    if laujin >= 0:
        users_data[laujin]['balance'] = users_data[laujin]['balance'] + int(nominal)
        os.system('cls')
        print('\033[92m')
        if __name__ == "__main__":
            with Loader("Transaksi Sedang Diproses..."):
                for i in range(10):
                    sleep(0.25)
        print(60*"=",'\033[0m')
        os.system('cls')
        os.system('cls')
        print('\033[92m')
        print(60*"=")
        print('')
        print("\t\t      Transaksi Berhasil".upper())
        print(f"  Anda Berhasil Menyetor Uang Sejumlah Rp.{nominal:,}".replace(",","."))
        print(60*"=")
        print('')
        print(f"\tTotal Saldo Anda Rp {users_data[laujin]['balance']:,}      ".replace(",","."))
        print('')
        print(60*"=","\033[0m")

def tarik(tarikan):
    debit_user = auth_id(authid)
    if debit_user >= 0:
        if users_data[debit_user]['balance'] >= int(tarikan):
            users_data[debit_user]['balance'] = users_data[debit_user]['balance'] - int(tarikan)
            os.system('cls')
            print('\033[92m')
            if __name__ == "__main__":
                with Loader("Transaksi Sedang Diproses..."):
                    for i in range(10):
                        sleep(0.25)
            print(60*"=",'\033[0m')
            os.system('cls')
            os.system('cls')
            print('\033[92m')
            print(60*"=")
            print("\t\t      Transaksi Berhasil".upper())
            print('')
            print(f"  Anda Berhasil Menarik Uang Sejumlah Rp.{tarikan:,}".replace(",","."))
            print('')
            print(60*"=")
            print('')
            print(f"\tSisa Saldo Anda Rp {users_data[debit_user]['balance']:,}      ".replace(",","."))
            print('')
            print(60*"=",'\033[0m')
        else:
            os.system('cls')
            print('\033[31m')
            if __name__ == "__main__":
                with Loader("Transaksi Gagal! Saldomu Gacukup!..."):
                    for i in range(10):
                        sleep(0.15)
            print(60*"=",'\033[0m')
            os.system('cls')
            os.system('cls')
            print('')
            print(60*"=")
            print('')
            print("\t\t   Saldo Anda Tidak Mencukupi")
            print('')
            print(f"\t\tSaldo Anda Saat ini Rp. {users_data[debit_user]['balance']}")
            print('')
            print(60*"=")
def pengguna():
    orang = auth_id(authid)
    if orang >=0:
        os.system('cls')
        print('\033[92m')
        if __name__ == "__main__":
            with Loader("Mengambil Info Pengguna..."):
                for i in range(10):
                    sleep(0.25)
        print(60*"=",'\033[0m')
        os.system('cls')
        print(60*"=")
        print('')
        print(f"Nama\t\t: {users_data[orang]['name']}")
        print(f"Username\t: {users_data[orang]['users']}")
        print(f"Pin\t\t: {users_data[orang]['pin']}")
        print(f"Nomer Rekening\t: {users_data[orang]['rekening']}\n")
        print(f"Total Saldo\t: {users_data[orang]['balance']}\n")
        print('')
        print(60*"=")

def alert():
    print('\033[31m')
    print("="*60)
    print(f"{'=== Data Yang Anda Masukkan Salah! Silahkan Cek Kembali. ===':^60}")
    print("="*60,'\033[0m',"\n")        

verif_id = 0
authid = 0
auth_user = False
orang = 0
next_step = False
while True:
    salam = "\n\n\t\tHai Selamat Datang Di Bankrupt 1.0"
    sapa(salam)
    time.sleep(1)
    os.system('cls') 
    salam = "\n\n\t\tProgram Ini Dibuat Oleh Achmad Ali Akbar \n\t\t\tKelas : INFORMATIKA A\n\t\t\tNim : D0222320\n\t\t\tUntuk Memenuhi Tugas DDP."
    sapa(salam)
    time.sleep(1)
    os.system('cls') 
    salam = "\n\n\t\tLangsung Saja Masuk Ke Program."
    sapa(salam)
    os.system('cls') 
    print('\033[92m')
    if __name__ == "__main__":
        with Loader("\t\tMengalihkan Halaman! ..."):
            for i in range(10):
                sleep(0.25)
    print(60*"=",'\033[0m')
    os.system('cls') 
    title()
    menu()
    pilih_menu = int(input("Silahkan Pilih Menu :  "))

    if pilih_menu == 1:
        auth_user == False
    elif pilih_menu == 2:
        auth_user == "Success"
        register()
    elif pilih_menu == 3:
        os.system('cls')
        print('\033[94m')
        print("Program Selesai Have a nice day ^__^")
        print('\033[0m')
        break

    else:
        print("Masukkan Pilihan Dengan Benar!")

    while auth_user == False:
        os.system('cls')
        title()
        print("\t\tMasukkan Username : ")
        usermu = input("\t\t\t")
        os.system('cls')
        title()
        print("\t\tMasukkan pin : ")
        pinmu = input("\t\t\t")
        cek_data = login_func(usermu,pinmu)
        if cek_data:
            os.system('cls')
            os.system('cls')
            print("\033[32m")
            if __name__ == "__main__":
                with Loader(f"Login Berhasil! Selamat Datang {cek_data['name']}"):
                    for i in range(10):
                        sleep(0.25)
            os.system('cls')
            print("\033[0m")
            auth_user = True
        else:
            os.system('cls')
            print('\033[31m')
            print("="*60)
            print(f"{'=== Data Yang Anda Masukkan Salah! Silahkan Cek Kembali. ===':^60}")
            print("="*60,'\033[0m',"\n")        
            time.sleep(3)
            auth_user = False
        
    while auth_user == True:
            title()
            cek_data = login_func(usermu,pinmu)
            if cek_data:
                print("="*60)
                print(f"{'================== Bank Krupt Mobile Bank ==================':^60}")
                print("="*60)
                print(f" {'Hai Selamat Datang':<40}{cek_data['name']:<40}")
                print("="*60,"\n")
                authid = cek_data['id']
                next_step = True
                auth_user = False
            else:
                print('')
                next_step = False
                auth_user = True
                    
    while next_step == True:
        os.system('cls')
        menu_user()
        print("Silahkan Memilih Menu Transaksi!")
        ngapain = int(input(40*""))
        os.system('cls')
        if ngapain == 1:
            os.system('cls')
            print(60*'-',"\n")
            print('Masukkan Rekening Tujuan')
            rek_tujuan = input('  ')
            print("\n",'-'*60)
            verif_rekening = auth_rek(rek_tujuan)
            if verif_rekening >=0:
                os.system('cls')
                print(60*'-',"\n")
                print('Masukkan Nominal Yang Ingin Di Transfer')
                nominal = int(input('  '))
                print("\n",'-'*60)
                if int(nominal)>= 10000:
                    transfer(nominal,rek_tujuan)
                    time.sleep(3)
                    next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                    os.system('cls')
                    if __name__ == "__main__":
                        with Loader("Sabar Bang ..."):
                            for i in range(10):
                                sleep(0.25)
                    os.system('cls')
                else:
                    print(60*'=')
                    print('')
                    print("\t\tNOMINAL TIDAK VALID / TRANSAKSI MINIMAL Rp. 10.000")
                    print('')
                    print(60*'=')
                    time.sleep(5)
                    os.system('cls')
            else:
                print(60*'=')
                print('')
                print("\t\tNOMOR REKENING TIDAK VALID")
                print('')
                print(60*'=')
                time.sleep(3)
                os.system('cls')
        elif ngapain == 2:
            cek_saldo()
            next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
            os.system('cls')
            if __name__ == "__main__":
                with Loader("Sabar Bang ..."):
                    for i in range(10):
                        sleep(0.25)
            os.system('cls')
        elif ngapain ==3:
            os.system('cls')
            print(60*'-',"\n")
            print('Masukkan Jumlah')
            nominal = int(input('  '))
            print("\n",'-'*60)
            if nominal >=10000:
                setoran(nominal)
                time.sleep(5)
                next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                os.system('cls')
            if __name__ == "__main__":
                with Loader("Sabar Bang ..."):
                    for i in range(10):
                        sleep(0.25)
                os.system('cls')
            else:
                print(60*'=')
                print('')
                print("\t\tNOMINAL TIDAK VALID / TRANSAKSI MINIMAL Rp. 10.000")
                print('')
                print(60*'=')
                time.sleep(5)
                next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                os.system('cls')
        elif ngapain ==4:
            os.system('cls')
            print(60*'-',"\n")
            print('Masukkan Jumlah')
            nominal = int(input('  '))
            print("\n",'-'*60)
            if nominal >=10000:
                tarik(nominal)
                time.sleep(5)
                next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                os.system('cls')
            if __name__ == "__main__":
                with Loader("Sabar Bang ..."):
                    for i in range(10):
                        sleep(0.25)
                os.system('cls')
            else:
                print(60*'=')
                print('')
                print("\t\tNOMINAL TIDAK VALID / TRANSAKSI MINIMAL Rp. 10.000")
                print('')
                print(60*'=')
                time.sleep(5)
                next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                os.system('cls')
            if __name__ == "__main__":
                with Loader("Sabar Bang ..."):
                    for i in range(10):
                        sleep(0.25)
                os.system('cls')
                os.system('cls')
        elif ngapain == 5:
                os.system('cls')
                pengguna()
                next_setep = input("Lanjut Transaksi Lainnya ? (Y/n) ")
                os.system('cls')
                if __name__ == "__main__":
                    with Loader("Sabar Bang ..."):
                        for i in range(10):
                            sleep(0.25)
                os.system('cls')
        elif ngapain == 6:
            print("\t\tYakin Ingin Log Out? ? (Y/n) ")
            next_setep = input("\t\t")
            os.system('cls')
            if next_setep == 'y' or next_setep == 'Y':
                os.system('cls')
                if __name__ == "__main__":
                    print("\033[32m")
                    with Loader("Anda Berhasil Log Out wait a sec ...",'\033[0m'):
                        for i in range(10):
                            sleep(0.25)
                    os.system('cls')
                    next_setep == False                 
                    break
            elif next_setep == 'n' or next_setep == 'N':
                next_setep == True
            









