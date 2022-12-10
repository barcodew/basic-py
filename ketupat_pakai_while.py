N = int(input("Masukkan Panjang : "))
count=0
spasi=N//2
if N%2==0:
    spasi-=1
while count<=N:
    if count%2==1:
        print(" "*spasi + "*"*count)
        spasi-=1
        count+=1
    else:
        count+=1
if N%2==0:
    count=N-2
else:
    count=N-1
spasi=1
if count%2==0:
    count-=1
while count>0:
    if count%2==1:
        print(" "*spasi + "*"*count)
        spasi+=1
        count-=1
    else:
        count-=1
