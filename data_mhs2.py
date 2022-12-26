import os
import datetime
import string
import random

template = {
        'nama':'nama',
        'nim':'nim',
        'jumlah_sks':0,
        'lahir': datetime.datetime(1111,11,11)
    }

data_mahasiswa = {

    }
while True:

    os.system('cls')
    print("-"*46)
    print("="*15,"Selamat Datang","="*15)
    print("="*7,"Silahkan Input Data Mahasiswa","="*7)
    print("-"*46)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['nama'] = input("Masukkan Nama Mahasiswa :")
    mahasiswa['nim'] = input("Masukkan Nim :")
    mahasiswa['jumlah_sks'] = int(input("Masukkan Jumlah Sks :"))
    TAHUN_LAHIR = int(input("Masukkan Tahun Lahir (YYYY) :"))
    BULAN_LAHIR = int(input("Masukkan Bulan Lahir (MM) :"))
    TANGGAL_LAHIR = int(input("Masukkan Tanggal Lahir (DD) :"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    print("-"*80)
    print("="*28,"Data - Data Mahasiswa ","="*28)
    print("-"*80)
    print(f"{'No.':<6} {'NAMA':<25} {'NIM':<18} {'JUMLSH SKS':<12} {'TANGGAL LAHIR':<16}")
    print('-'*80,"\n")
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        JUMLAH_SKS = data_mahasiswa[KEY] ['jumlah_sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY} {NAMA:<25} {NIM:<18} {JUMLAH_SKS:^12} {LAHIR:^16}\n")
    print('-'*80,"")
    print('-'*80,"\n")

    lanjut = input("\nLanjut Menginput Data? (Y/n) :")
    if lanjut == "n":
        break
os.system('cls')
print("-"*80)
print("="*28,"Data - Data Mahasiswa ","="*28)
print("-"*80)
print(f"{'No.':<6} {'NAMA':<25} {'NIM':<18} {'JUMLSH SKS':<12} {'TANGGAL LAHIR':<16}")
print('-'*80,"\n")
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    JUMLAH_SKS = data_mahasiswa[KEY] ['jumlah_sks']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY} {NAMA:<25} {NIM:<18} {JUMLAH_SKS:^12} {LAHIR:^16}\n")
print('-'*80,"")
print('-'*80,"\n")

print("Program Selesai!") 
