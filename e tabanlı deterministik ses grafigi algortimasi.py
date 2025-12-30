import matplotlib.pyplot as plt  
import winsound as _ws
from time import sleep as _sl
import math as mat

nQ = 256
sec = 6

input_array = [int(n*mat.e) for n in range(nQ)]
output_array = []
freq_array = []

print('Input array: {}'.format(input_array))

if input_array:
    if input_array != []:
        if isinstance(input_array,list):
            for argument in input_array:
                q = [list(str(argument).encode())]
                for deep_argument in q:
                    qout = [x for x in list((str(deep_argument).encode()))]
                    output_array.append([sum(qout) / len(qout),input_array.index(argument)])
                
new_arr = [input_array[ix[1]] for ix in sorted(output_array)]

print(new_arr)

fig,ax = plt.subplots(2,1)

ax[0].axhline(nQ // 2,color='black')
ax[0].axvline(nQ // 2,color='black')
ax[0].set_title('Orjinal array'),
for freq in input_array:
    if freq > 37:
        _ws.Beep(freq,sec)
        
        ax[0].clear()
        ax[0].plot(freq_array)

        freq_array.append(freq)

        plt.pause(sec / 100)

freq_array.clear()
_sl(2.4)

ax[1].axhline(nQ // 2,color='black')
ax[1].axvline(nQ // 2,color='black')
ax[1].set_title('Orjinal array'),
for freq in new_arr:
    if freq > 37:
        _ws.Beep(freq,sec)
        
        ax[1].clear()
        ax[1].plot(freq_array)

        freq_array.append(freq)

        plt.pause(sec / 100)


plt.show()
