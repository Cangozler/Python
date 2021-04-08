toplam=0

while(True):
    sayi=int(input("Lütfen Bir Sayı Giriniz :"))
    if(sayi==-1):
        break

    if(sayi%7==0):
        print(sayi,"7 ye tam bölünür...")
    else:
        print(sayi,"sayı 7 ye tam bölünmez...")

    toplam+=sayi

print("Girilen Sayıların Toplamı : ",toplam)