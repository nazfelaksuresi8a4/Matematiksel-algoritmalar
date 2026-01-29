def max_(dizi):
    en_iyi_eleman_indeksi = 0
    en_iyi_eleman = 0

    for eleman in dizi:

        if dizi.index(eleman) == 0:
            elemanX = eleman
        
        elif eleman < elemanX:
            elemanX = eleman

    return elemanX
            
maksimum = max_([6,14,614,62,46,357,35])
print(maksimum)
