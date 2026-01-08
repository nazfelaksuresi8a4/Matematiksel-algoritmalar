import numpy as np 
import matplotlib.pyplot as plt

def f(x,arr):
    index = arr.index(x)

    if x >= 10:
        x = x - x 
        print('h')
            
    elif x <= 0:
        x + 1
            
    elif x == 5:
        x = x - (x + 1)
        print(x)
    
    if index >= len(arr) // 2:
        x = abs(x)

    arr[index] = x

term_arr = [10,5,10]*(4*2)

for term in term_arr:
    f(term,term_arr)

NDarray = np.array(term_arr)

print(NDarray)

fig,ax = plt.subplots(1,1)
ax.axhline(0,color='black')
ax.axvline(len(NDarray) // 2,color='black')
ax.plot(NDarray,c='black',linewidth=0.5,linestyle='--')
plt.show()
