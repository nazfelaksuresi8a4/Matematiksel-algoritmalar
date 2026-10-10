import matplotlib.pyplot as plt 
from math import sqrt

x = [10,20,30,500,400,300]

N = len(x)
mu = sum(x) / N
a_ = sqrt(sum([((Xa - mu)**2) / N for Xa in x]))

z_toleransi = 1.3

elemanlar_ve_skorlar = {Xi : abs((Xi - mu) / a_) for Xi in x}

def filter_function(x_):
    global elemanlar_ve_skorlar

    if elemanlar_ve_skorlar[x_] > z_toleransi:
        return 1

    else : return 0

filtrelenmis_aykiri_elemanlar = filter(filter_function, elemanlar_ve_skorlar)

for key in filtrelenmis_aykiri_elemanlar:
    print('eleman: {} || z-skoru: {}'.format(key,elemanlar_ve_skorlar[key]))

x_axis,y_axis = [key for key in elemanlar_ve_skorlar],[elemanlar_ve_skorlar[key] for key in elemanlar_ve_skorlar]

yline,xline = -z_toleransi,z_toleransi

plt.axhline(xline,color='black')
plt.axvline(yline,color='black')
plt.xlabel('elemanlar')
plt.ylabel('z-skorlari')
plt.plot(x_axis,y_axis)

plt.show()
