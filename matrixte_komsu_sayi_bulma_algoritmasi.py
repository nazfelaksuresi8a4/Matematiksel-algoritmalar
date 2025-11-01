#Bu algoritma bir matrix gridinde "target, neighbour" şeklinde komşı sayıları hem dikte(y) hemde yatay(x) şekilde tarayarak bulabilir


paths = []

def find(matrix,target,neighbors,shape=None):
    n = len(matrix)
    
    if shape is not None:
        if shape == "x-axis":
            for i in range(0,n):
                for j in range(1,len(matrix[i])):
                    if matrix[i][j - 1] == target and matrix[i][j] == neighbor:
                        paths.append((matrix[i][j - 1], matrix[i][j])) 
                
        
        elif shape == "y-axis":
            for i in range(1, n):
                for j in range(1, len(matrix[i])):
                    if matrix[i - 1][j - 1] == target and matrix[i][j - 1] == neighbor:
                        paths.append((matrix[i - 1][j - 1], matrix[i][j - 1])) 
        
        return paths
    
    else:
        print("Lütfen geçerli bir yön seçin!! ") 
        
matrix = [[1,0,1,4,0,0],
          [4,0,0,3,5,9]]   
target = 1
neighbor = 4
shape = "y-axis"

path_output = find(matrix, target, neighbor,shape) 

print(path_output)  