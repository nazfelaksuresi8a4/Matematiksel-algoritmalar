from math import sqrt

x = [10,20,30,500,400,300]

N = len(x)
mu = sum(x) / N
a_ = sqrt(sum([((Xa - mu)**2) / N for Xa in x]))

z_toleransi = 1.3

aykiri_elemanlar = {Xi : abs((Xi - mu) / a_) for Xi in x}

def filter_function(x_):
    global aykiri_elemanlar

    if aykiri_elemanlar[x_] > z_toleransi:
        return 1

    else : return 0

filtrelenmis_aykiri_elemanlar = filter(filter_function, aykiri_elemanlar)

for key in filtrelenmis_aykiri_elemanlar:
    print('eleman: {} || z-skoru: {}'.format(key,aykiri_elemanlar[key]))

