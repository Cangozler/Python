bas= int(input("baslangıc degeri giriniz"))
bit= int(input(" bitiş değeri giriniz"))
bol=int( input( "bölünecek sayiyi giriniz"))
for i in range(bas,bit):
       if i% bol==0:
           print(i)