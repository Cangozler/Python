import os
selection=0
while(selection!=4):
    selection = int(input("Yapmak istedi�iniz i�lem \n 1-Kay�t \n 2-Arama \n 3-Kay�t silme \n 4-��k��"))
    if selection==1:
        if os.path.exists("�grenci.txt"):
            print("�grenci.txt dosyas� bulunamad�, dosya olu�turuluyor")
            dosya=open("�grenci.txt","w")
            ad=input("��renci ad�:")
            telno=input("Telefon numras�:")
            okul=input("Okulu:")
            odano=input("Oda numaras�:")
            toplamborc=input("Toplam borcu:")
            taksitsay=input("Taksit say�s�:")
            taksittutar=input("Taksit tutar�:")
            print("Ad",ad,"Telno",telno,"okul",okul,"odano",odano,"toplamborc",toplamborc,"taksitsay",taksitsay,"taksittutar",taksittutar,file=dosya)
        else:
            dosya=open("�grenci.txt","w")
            ad=input("��renci ad�:")
            telno=input("Telefon numras�:")
            okul=input("Okulu:")
            odano=input("Oda numaras�:")
            toplamborc=input("Toplam borcu:")
            taksitsay=input("Taksit say�s�:")
            taksittutar=input("Taksit tutar�:")
            print("Ad",ad,"Telno",telno,"okul",okul,"odano",odano,"toplamborc",toplamborc,"taksitsay",taksitsay,"taksittutar",taksittutar,file=dosya)
    elif selection ==2:
        if os.path.exists("�grenci.txt"):
            ara=input("��rencinin ad�n� yada Telefon numaras�n� giriniz")
            dosya=open("�grenci.txt","r")
            zz = 0
            for a in dosya:
                if ara == zz:
                    print(a)
                zz+=1
            dosya.close()
        else:
            print("Dosya bulunamad� �nce olu�turun")
    elif selection ==3:
            dosya = open("�grenci.txt", "r")
            ara=input("��rencinin ad�n� yada Telefon numaras�n� giriniz")
            satirlar = dosya.readlines()
            dosya.close()

            yenidosya = open("�grenci.txt", "w")
            for satir in satirlar:
                if satir.find(ara)==False:
                    yenidosya.write(satir)
            yenidosya.close()
    else:
        print("program kapat�l�yor")
        break