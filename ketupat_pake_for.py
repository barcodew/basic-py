panjang = int(input("Masukkan Panjang : "))


for i in range(panjang):
    for spasi in range(panjang-i-1):
        print(" ",end = " ")
    for bintang in range(2*i+1):
        print("+",end= " ")
    print()
for k in range(panjang-1,0,-1):
    for spasi in range(panjang-k):
        print(" ",end=" ")
    for bintang in range(2*k-1):
        print("+",end=" ")
    print()
