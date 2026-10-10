from math import sqrt

x = [10,20,30,500,400,300]

i = 0
z_tolerance = 1.

while True:
    i = 0 

    if len(x) > 0:
        mu = sum(x) / len(x)    
        sigma = sqrt(sum([((Xi - mu)**2)/len(x) for Xi in x]))  

        yeni = []  

        while i < len(x):   
            if sigma > 0:
                z_score = (x[i] - mu) / sigma

                if abs(z_score) < z_tolerance:
                    yeni.append(x[i])        

            else:
                yeni.append(x[i])

            i += 1

        if len(x) == len(yeni):
            break

        x = yeni    

    else:
        print('iteratif hesaplamada tüm değerler aykırı çıktı')
        break

print(x)
