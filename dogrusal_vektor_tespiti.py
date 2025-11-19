#**1**#
#Bu kod sadece bir prototipi temsil eder gerçek projelerde daha güvenli versiyonları kullanılmaktadır, kullanılmalıdır!!!! 

T = 1   #T sabiti 
index = 0
K = [1,2,3,4,5,4,4,6]

for i in range(len(K)):
    if K[i] - K[i - 1] = R:
        index += 1
    
if index == len(K) - 1:
    print("Vektör doğrusal") 

else:
    print("vektör doğrusal değil") 

#Daha güvenli ve anlaşılır bir şekilde yazacak olursak;

import matplotlib.pyplot as plt
import numpy as np

#

def GetLinearRange(xVector,xLength,xAction):
    try:
        if xAction:
            if xAction == 'pop-false':
                index,start,flag,stat = 0,0,True,False
                T = 1 

                for i in range(1,len(xVector)):
                    if np.abs(xVector[i] - xVector[i - 1]) == T:
                        index += 1

                        if flag == False:
                            start = i
                            flag = True


                if index == xLength - 1:
                    print('Vektör Tamamen Doğrusal')

                else:
                    if isinstance(start,int):
                        vector = xVector[start:index - 1]
                        print(vector)

                        stat = True
                        
                    else:
                        print('Error')

                if stat == True:
                    print(f'Bozulma sonrası kalan veriler: {xLength - index}\nKaç ile kaç arasında doğrusal: {vector[0]}....{vector[len(vector) - 1]}\nDoğrusal veri ortalaması:{np.mean(np.array(vector))}')

                else:
                    if stat:
                        if stat != True:
                            print(f'Bozulma sonrası kalan veriler: {xLength - index}\nKaç ile kaç arasında doğrusal: {xVector[0]}....{xVector[len(xVector) - 1]}\nDoğrusal veri ortalaması:{np.mean(np.array(xVector))}')

            elif xAction == 'pop-true':
                index,start,flag,stat = 0,0,True,False
                T = 1 

                for i in range(1,len(xVector)):
                    if i != xLength - 1:
                        if isinstance(xVector[i],int) and isinstance(xVector[i - 1],int):
                            if np.abs(xVector[i] - xVector[i - 1]) == T:
                                index += 1

                            else:
                                xVector[i] = '#'
                        
                        else:
                            pass
                
                for j in xVector:
                    if j == '#':
                        xVector.pop(xVector.index(j))

                print(xVector)

    except Exception as nException:
        print('finally-exception-line-excepiton: ' + str(nException))
        

aVector = [1,2,3,4,5,6,7,8,19,9,10,11]
aLength = len(aVector)
aAction = 'pop-true'

AlgorithmFunction = GetLinearRange(aVector,aLength,aAction)

