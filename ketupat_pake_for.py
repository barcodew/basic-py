def ketupat(pat):

    for i in range(pat):
        for spasi in range(pat-i-1):
            print(" ",end=" ")
        for plus in range(2*i+1):
            print("+",end=" ")
        print()
    for a in range(pat-1,0,-1):
        for spasi in range(pat-a):
            print(' ',end=" ")
        for plus in range(2*a-1):
            print("+",end=" ")
        print()
panjang = int(input("Masukkan Panjang : "))

ketupat(panjang)
