input_array = [0,1,2,3,4,5,6]
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
