def bul(dizi,hedef):
    n = len(dizi)

    for i in range(1,n):
        if (hedef - dizi[i]) in dizi:
            return dizi.index(hedef - dizi[i]),i 
        
hedef = 9
dizi = [7, 0, 1, 2]

sonuc = bul(dizi,hedef)

print(sonuc)
