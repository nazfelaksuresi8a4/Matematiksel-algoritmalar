def say(dizi):
    frekanslar = {}

    for i,sayi in enumerate(dizi):
        frekanslar[sayi] = frekanslar.get(sayi,0) + 1

    return frekanslar


dizi = [1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,5,6]

cikti = say(dizi)

print(cikti)

def say(dizi):
    frekanslar = {}

    for i,sayi in enumerate(dizi):
        if sayi in frekanslar:
            frekanslar[sayi] += 1

        else:
            frekanslar[sayi] = 1

    return frekanslar


dizi = [1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,5,6]

cikti = say(dizi)

print(cikti)
