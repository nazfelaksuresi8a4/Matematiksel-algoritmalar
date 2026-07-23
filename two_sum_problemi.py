def bul(dizi,hedef):
    n = len(dizi)

    for i in range(1,n):
        if (hedef - dizi[i]) in dizi:
            return dizi.index(hedef - dizi[i]),i 
        
hedef = 9
dizi = [7, 0, 1, 2]

sonuc = bul(dizi,hedef)

print(sonuc)

#yukarıdaki çözüm yanlıştır çünkü 'in' 'dizi.index' gibi fonksiyonlar ve anahtarlar diziyi baştan sona gezer ve karmaşıklık O(n^2) olur  aynı şeyi O(n^2) algoritmasında yaparsak ise bu sefer O(n^3) olup yine hatalı olurdu.
#diğer bir hata ise 1 den başlşayan döngü ve elemanların kendini görme riskidir aynı 
#doğru çözümn O(n) ve O(n^2) için aşşağıdaki gibidir 

#O(n) çözüm 

def bul(dizi,hedef):
    gorulenler = {}

    for i,num in enumerate(dizi):
        kalan = hedef - num

        if kalan in gorulenler:
            return gorulenler[kalan],i

        gorulenler[num] = i

    return -1

dizi = [6,2,6472,72,754,75,275,257,257,2]
hedef = (72+257)

sonuc = bul(dizi,hedef)

print(sonuc)

#O(n^2) çözüm

def bul(dizi,hedef):
    n = len(dizi)

    for i in range(n):
        for j in range(i+1,n):
            if dizi[i] + dizi[j] == hedef:
                return i,j

dizi = [6,2,6472,72,754,75,275,257,257,2]
hedef = (72+257)

sonuc = bul(dizi,hedef)

print(sonuc)
