isim1 = input("İsmin : ")
isim2 = input("Sevdiğin kişinin ismi: ")

aşk = len(isim1) + len(isim2)

if len(isim1) > len(isim2):
    aşk -= 8
else:
    aşk += 5

aşk *= 42
aşk = aşk / (100 + len(isim2))

aşk = 10 if aşk > 10 else round(aşk, 0)

print("{} sevgilin olan {} seni  10 üzerincden bu kadar seviyor {}  ".format(isim1, isim2, aşk))