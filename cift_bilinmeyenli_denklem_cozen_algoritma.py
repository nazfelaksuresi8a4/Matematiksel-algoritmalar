import time

""" User Input Side """
denklem = str(input("> "))

x1 = 1
x2 = 1
arrindex = 0
loop_index = 1 
frame = 100

splitted = denklem.split()

equality = splitted.pop()
nums = []
symbols = []
arr = [] 

for m in splitted:
    if m.replace("x","").isdigit() == True:
        arr.append([]) 

matrix_length = len(arr) 


""" Number Parser Side """
for xi in range(len(splitted)):
    if not splitted[xi].replace('x','').isdigit() == True:
        symbols.append(splitted[xi].replace('x',''))
         
    if splitted[xi].replace("x","").isdigit() == True:
        arr[arrindex].append(int(splitted[xi].replace("x", "").strip()))
        
        arrindex += 1
        

#arr = num
#symbols = symbols

"""Solver Side"""
for symindex,numindex in zip(range(len(symbols)),range(len(arr))):
    if symbols[symindex] == '-':
        while int(arr[numindex][0])*x1 - int(arr[loop_index][0])*x2 != int(equality):
            if x2 != frame:
                x2 += 1
            
            else:
                if frame == 500:
                    frame = 500
                
                else:
                    frame *= 2

                x2 = 1
                x1 += 1

print(f'Denklem: {denklem}\nÇözüm: x1 = {x1}, x2 = {x2}')




    
    
