print('='*10,'Sign Up','='*10)
user_regist = input('Masukkan Username :')
pass_regist = input('Masukkan Password :')

def login (user_pass,pass_word):
    if user_pass == user_regist and pass_word == pass_regist:
        status = True
    else :
        status = False
    return status

sesi = 0
while sesi <=3:
    print('='*10,'Login Page','='*10)
    username = input('Masukkan Username :')
    password = input('Masukkan Password :')
    status = login(username,password)
    if status == True:
        print('='*8,'Login Berhasil!','='*8)
        print(f'Selamat Datang {username}!')
        break
    elif status == False:
        print('='*8,'Login Gagal!','='*8)
        print(f'Username Dan Password Salah! Sisa Kesempatan {3-sesi}'.replace('0','Sudah Habis!'))
        sesi += 1
else:
    print('Silahkan Memulai Ulang Program!')
