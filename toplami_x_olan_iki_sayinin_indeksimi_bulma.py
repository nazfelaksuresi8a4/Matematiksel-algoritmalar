
#O(n^2) çözüm

def f(arr,x):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if  x - arr[j] in arr:
                return(arr[j],x-arr[j]) 


arr = [29,20]    

print(f(arr, 49)) 



#O(n) çözüm

def f(arr, x):
    cache = {} 
    
    for i, num in enumerate(arr):
      if x - num in cache:
          return cache[num-1], i
      
      cache[num] = i  
    
    return -1  

arr = [1, 2,2,2,3]

print(f(arr, 58))
