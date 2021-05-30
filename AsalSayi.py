liste=list()
liste.append()
sayi=3
while True:
    sayilar=True
    for i in range(2,sayi):
        if sayi %i ==0:
         sayilar=False
        break
    if sayilar:
        liste.append(sayi)
        if len(liste) == 100:
         break
        sayi += 1 
print(liste)        

