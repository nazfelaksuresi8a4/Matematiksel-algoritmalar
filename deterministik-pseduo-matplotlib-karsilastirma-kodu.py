import matplotlib.pyplot as plt  

nQ = 256

input_array = [n for n in range(nQ)]
output_array = []

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

fig,ax = plt.subplots(1,2)

ax[0].axhline(nQ // 2,color='black')
ax[0].axvline(nQ // 2,color='black')
ax[0].set_title('Orjinal array')
ax[0].plot(input_array)

ax[1].axhline(nQ // 2,color='black')
ax[1].axvline(nQ // 2,color='black')
ax[1].set_title('Deterministkik array')
ax[1].plot(new_arr)

plt.show()
