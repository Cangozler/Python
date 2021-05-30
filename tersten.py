def reverse(deger, output=[]):
    for i in range(len(deger) - 1, -1, -1):
        output.append(deger[i])
    
    return "".join(output)

text = input("Metin gir : ")
print("Terstenn: {}".format(reverse(text)))