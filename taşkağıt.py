import random

print(("-" * 30) + "\nKağıt, Taş, Makas \n" + ("-" * 30))

Kullanıcı_Skoru, Bilgisayarın_skoru = 0, 0

while True:
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    print("\n -Çıkmak için -4- tuşuna basınız")
    Kullanıcı_Seçimi = input("Seçimin: ")
    Bilgisayarın_Seçimi = random.choice(["1", "2", "3"])
    if Kullanıcı_Seçimi =="4":
        break
    if Kullanıcı_Seçimi == "1":
        if Bilgisayarın_Seçimi == "1":
            print("Bilgisayarın seçimi: Taş\nberabere!")
            
        elif Bilgisayarın_Seçimi == "2":
            print("Bilgisayarın_Seçimi: Kağıt\nKağıt taşı sarar. Kaybettin!")
            Bilgisayarın_skoru += 100
            
        elif Bilgisayarın_Seçimi == "3":
            print("Bilgisayarın_Seçimi: Makas\nTaş makası ezer. Kazandın!")
            Kullanıcı_Skoru += 100
            
    elif Kullanıcı_Seçimi == "2":
        if Bilgisayarın_Seçimi == "1":
            print("Bilgisayarın_Seçimi: Taş\nKağıt taşı sarar. Kazandın!")
            Kullanıcı_Skoru += 100
            
        elif Bilgisayarın_Seçimi == "2":
            print("Bilgisayarın_Seçimi: Kağıt\nberabere!")
            
        elif Bilgisayarın_Seçimi == "3":
            print("Bilgisayarın_Seçimi: Makas\nMakas kağıdı keser, kaybettin!")
            Bilgisayarın_skoru += 100
            
    elif Kullanıcı_Seçimi == "3":
        if Bilgisayarın_Seçimi == "1":
            print("Bilgisayarın_Seçimi: Taş\nTaş makası ezer kaybettin!")
            Bilgisayarın_skoru += 100
            
        elif Bilgisayarın_Seçimi == "2":
            print("Bilgisayarın_Seçimi: Kağıt\nMakas kağıdı keser, Kazandın!")
            Kullanıcı_Skoru += 100
            
        elif Bilgisayarın_Seçimi == "3":
            print("Bilgisayarın_Seçimi: Makas\nBerabere!")
    
    else:
        break
    
print("\n'Kullanıcı_Seçimi: {}\nBilgisayrın's skoru: {}".format(Kullanıcı_Skoru, Bilgisayarın_skoru))