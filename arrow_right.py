angka = 0
while angka  <= 10:
    if angka >= 0 or angka <= 5:
        print("   "*10,"**"*angka)
        angka +=1
        if angka >= 6:
            print("***"*10,"**"*angka)
            angka +=1

while angka >= 0:
    if angka >= 7 or angka <= 10:
        print("   "*10,"**"*angka)
        angka -=1
        if angka >= 6:
            print("***"*10,"**"*angka)
            angka -=1
