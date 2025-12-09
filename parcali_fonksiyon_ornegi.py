#f(x) = {2x x < 3; 3x x >=3} f1 + f2 + ... f8 = sum
def f(x):
    if x < 2:
        return 2*x
    if x >= 3:
        return 3*x
        
array = [0,5,10]
result = []

for _ in array:
    result.append(f(_)) 

output = sum(result) 

print(output) 
    