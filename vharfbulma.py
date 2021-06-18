Cumlemiz = input ("Bir cümle giriniz : ")
aranacak_Harf = input ("Aranacak Karakteri Giriniz : ")
toplam_Harf_Sayisi = 0

for i in Cumlemiz:
    toplam_Harf_Sayisi+1
    for b in i:
        if b in aranacak_Harf:
            toplam_Harf_Sayisi +=1
print("toplam istenilen sayı: {}".format(toplam_Harf_Sayisi))