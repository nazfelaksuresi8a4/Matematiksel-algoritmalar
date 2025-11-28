denklem = str(input("> "))

x1 = 1
x2 = 1

splitted = denklem.split()

equality = splitted.pop()
nums = []
arr = [] 

for sayi in splitted:
    if sayi[0].isdigit():
        n = len(sayi)
        
        try:
            for recnum in range(n):
                if sayi[recnum].isdigit() == True:
                    arr.clear() 
                    arr.append(sayi[recnum])
        
            for arrnum in arr:
                nums.append(int("".join([arrnum])))
                
        except Exception as e0:
            print(f"Parser Exception with line 26: {e0}") 
                
print(nums)
