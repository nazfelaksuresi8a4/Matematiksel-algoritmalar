def asal_filtresi(sayi):
    flag = True

    if sayi < 2:
        return False
    
    if sayi == 2:
        return True

    elif sayi %2 == 0:
        return False
    
    for term in range(3,int(sayi/2)):
        if sayi % term == 0:
            flag =  False
    
    return flag

        
    
vektör = [1,2,3,4,5,6,7,8,9,10,11]

filtrelenmis_vektör = filter(asal_filtresi,vektör)

print([eleman for eleman in filtrelenmis_vektör])
