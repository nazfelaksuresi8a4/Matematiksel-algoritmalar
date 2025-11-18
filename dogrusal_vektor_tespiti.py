#**1**#
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
    
    

#**2**#
#Bu kodun daha güvenli halde yazılması gerekirse; şu şekilde bir yol izlenebilir;

index = 0
K = [1,2,3,4,5,4,4,6]

tİnput = str(input("Artış doğrusallığı: ")) 
T = None

if tİnput.isdigit() == True:
    try:
        T = int(tİnput) 
    except Exception as tException:
        T = None
        print(tException) 

if T:
    if T is not None:
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
    
    


    