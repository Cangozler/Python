import os
selection=0
while(selection!=4):
    selection = int(input("Yapmak istediðiniz iþlem \n 1-Kayýt \n 2-Arama \n 3-Kayýt silme \n 4-Çýkýþ"))
    if selection==1:
        if os.path.exists("ögrenci.txt"):
            print("ögrenci.txt dosyasý bulunamadý, dosya oluþturuluyor")
            dosya=open("ögrenci.txt","w")
            ad=input("Öðrenci adý:")
            telno=input("Telefon numrasý:")
            okul=input("Okulu:")
            odano=input("Oda numarasý:")
            toplamborc=input("Toplam borcu:")
            taksitsay=input("Taksit sayýsý:")
            taksittutar=input("Taksit tutarý:")
            print("Ad",ad,"Telno",telno,"okul",okul,"odano",odano,"toplamborc",toplamborc,"taksitsay",taksitsay,"taksittutar",taksittutar,file=dosya)
        else:
            dosya=open("ögrenci.txt","w")
            ad=input("Öðrenci adý:")
            telno=input("Telefon numrasý:")
            okul=input("Okulu:")
            odano=input("Oda numarasý:")
            toplamborc=input("Toplam borcu:")
            taksitsay=input("Taksit sayýsý:")
            taksittutar=input("Taksit tutarý:")
            print("Ad",ad,"Telno",telno,"okul",okul,"odano",odano,"toplamborc",toplamborc,"taksitsay",taksitsay,"taksittutar",taksittutar,file=dosya)
    elif selection ==2:
        if os.path.exists("ögrenci.txt"):
            ara=input("Öðrencinin adýný yada Telefon numarasýný giriniz")
            dosya=open("ögrenci.txt","r")
            zz = 0
            for a in dosya:
                if ara == zz:
                    print(a)
                zz+=1
            dosya.close()
        else:
            print("Dosya bulunamadý önce oluþturun")
    elif selection ==3:
            dosya = open("ögrenci.txt", "r")
            ara=input("Öðrencinin adýný yada Telefon numarasýný giriniz")
            satirlar = dosya.readlines()
            dosya.close()

            yenidosya = open("ögrenci.txt", "w")
            for satir in satirlar:
                if satir.find(ara)==False:
                    yenidosya.write(satir)
            yenidosya.close()
    else:
        print("program kapatýlýyor")
        break