import random
import string

def generate_password(Uzunluk, seviye, output=[]):
    chars = string.ascii_letters
    if seviye > 1:
        chars = "{}{}".format(chars, string.digits)
    if seviye > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(Uzunluk):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("*" * 20) + "\n Şifre oluşturucusuna hoşgeldiniz\n" + ("*" * 20))
print(("-" * 30) + "\n Uzunluk ve seviye seçerek şifrenizi oluştrabilirsiniz\n" + ("-" * 30))

sifre_Uzunlugu = int(input("Uzunluk seciniz: "))
sifre_seviyesi = int(input("seviye seciniz 1 veya 2: "))
password = generate_password(sifre_Uzunlugu, sifre_seviyesi)
print("\nŞifren: {}".format(password))