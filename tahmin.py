from random import randint

rand=randint(1,7)
sayac=0
while True:
    sayac==3
    sayi=int(input("1 ile 7 arsı değer gir (-1 çıkış): "))
    if(sayi==-1):
        print("Oyunu iptal ettin")
        break
    elif(sayi==7):
         print("Tebrikler doğru tahmin".format(rand))  
         break
    elif sayi<rand:
        print("yaklaştık çık biraz")
        continue
    elif sayi>rand:
        print("yüksek biraz in")
        continue
    elif (sayac==3):
        print("tahmin hakkınız kalmadı {0}".format(sayac))
        break
    else:
        print("rastgele seçilen sayı {0}!".format(rand))
        print("tahmin sayını {0}".format(sayac))
        