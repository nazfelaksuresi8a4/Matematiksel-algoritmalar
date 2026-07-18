'''Matriste köşegen nası alınır (soru işareti koyamıyom bozuldu)'''

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n = len(mat)

'''
    MOD         DİV
0 % 4 = 0     0 // 4 = 0
1 % 4 = 1     1 // 4 = 0
2 % 4 = 2     2 // 4 = 0
3 % 4 = 3     3 // 4 = 0

Div -> sütun indeksi (dikey)
Mod -> satır indeksi (yatay)

matrix[DIVx][MODx]

'''

'''
for i in range(n):
    col = (i % n)
    
    num = mat[n-(i+1)][col] #düz köşegen
    num = mat[n-1][col]     #ters köşegen

'''

'''
for i in range(n):
    duz_kosegen = mat[i][i]
    ters_kosegen = mat[i][n - i - 1]

    print()
'''
