#Bu kod sadece bir prototipi temsil eder gerçek projelerde daha güvenli versiyonları kullanılmaktadır, kullanılmalıdır!!!! 

index = 0
K = [1,2,3,4,5,4,4,6]

for i in range(len(K)):
    if K[i - 1] + 1 == K[i]:
        index += 1
    
if index == len(K) - 1:
    print("Vektör doğrusal") 

else:
    val = ((len(K) - 1)) 
    vector = K[0:val]
    
    t1, tN= vector[0], vector[len(vector) - 1]
    
    print(f"Kaç kaça kadar doğrusal: {t1}....{tN}") 
    
    


    