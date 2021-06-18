def enbuyuk(liste1):
    sayi = max(liste1)
    return sayi
def enkucuk(liste1):
    sayi = min(liste1)
    return sayi
liste=[]
adet=int(input("kaç adet sayı girmek istiyon  :"))
for n in range(adet):
    sayi = int(input('Sayıyı Gir:  '))
    liste.append(sayi)

print("en buyuk sayi",enbuyuk(liste) , "en küçük sayı",enkucuk(liste))