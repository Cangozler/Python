isim=[]
vize=[]
final=[]
ortalama=[]
durum=[]
for i in range(3):
    ad=input("ad girniz:")
    isim.append(ad)
    viz=int(input("vize notunu girinizİ"))
    vize.append(viz)
    fin=int(input("final notunu giriniz:"))
    final.append(fin)
    ort=viz0.4+fin0.6
    ortalama.append(ort)

if ort<60:
         sonuc="kaldı"
else:
         sonuc="geçti"
         durum.appdend(sonuc)
         
ogrenci=open("c:/deneme/ogrenci.txt","w")
ogrenci.write("{:<30}{:^10}{:^10}{:^10}{:^10}".format("adı soyadı","final","vize","ortalama","sonuç"))
ogrenci.write("\n")
for i in range(3):

 ogrenci.write("{:<30}{:^10}{:^10}{:^10}{:^10}".format(isim[i],vize[i],final[i],ortalama[i],sonuc[i]))
ogrenci.write()
ogrenci.close()