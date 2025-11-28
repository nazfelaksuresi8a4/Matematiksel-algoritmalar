""" User Input Side """
denklem = str(input("> "))

x1 = 1
x2 = 1
arrindex = 0

splitted = denklem.split()

equality = splitted.pop()
nums = []
arr = [] 

for m in splitted:
    if m.replace("x","").isdigit() == True:
        arr.append([]) 

matrix_length = len(arr) 


""" Number Parser Side """
for xi in range(len(splitted)):
    if splitted[xi].replace("x","").isdigit() == True:
        arr[arrindex].append(int(splitted[xi].replace("x", "").strip()))
        
        arrindex += 1

print(arr)     
        
    
    