"""" X: dağın x eksenindeki uzunluk vektörü
     Y: dağın y eksenindeki uzunluk vektörü
     Z: dağın z eksenindeki konum  vekörü
     
     Xv, Tv, Zv: yukarıdaki vektörlerin sırası ile eş uzunlukta yön vektörleri
     
     Zp: Zero Point olarak geçer dağın 0 noktası"""

"""değişim eşiği = yön vektör dağılım farkları eşitliği sağlanırsa
dağın yön dağılımı arasınaki fark = 0 olmalıdır bu yüzdende 
eşikler kendi aralarında bu eşitliği sağlarsa yön vektörler farkına 
bakmak yerine şekil farkına göre yorumlama yapmak gerekir."""

"""Eski versiyonda eşikler bu şekilde çıkınca eşitlik sağlanırdı. 
ancak yeni versiyonda yön vektörü sınırsız float döner aynı şartlar 
buradada geçerlidir sadece veri tipi değişmiştir"""


def m(X, Y, Z, Xv, Yv, Zv, Zp):
    Xf = sum([ max([X[nx-1],X[nx] ]) - min([ X[nx-1],X[nx] ]) for nx in range(1,len(X))]) 
    Yf = sum([ max([Y[ny-1],Y[ny] ]) - min([ Y[ny-1],Y[ny] ]) for ny in range(1,len(Y))]) 
    Zf = sum([max([Z[nz-1],Z[nz] ]) - min([ Z[nz-1],Z[nz] ]) for nz in range(1,len(Z))]) 
    
    Xvf = sum([max([ Xv[nx-1],Xv[nx] ]) - min([ Xv[nx-1],Xv[nx] ]) for nx in range(1,len(Xv))]) 
    Yvf = sum([max([ Yv[ny-1],Yv[ny] ]) - min([ Yv[ny-1],Yv[ny] ]) for ny in range(1,len(Yv))]) 
    Zvf = sum([max([ Zv[nz-1],Zv[nz] ]) - min([ Zv[nz-1],Zv[nz] ]) for nz in range(1,len(Zv))])
    
    XYZVt = Xvf + Yvf + Zvf
    XYZt = Xf + Yf + Zf
    
    if XYZVt <= 0:
        thresh = float("inf") 
        
    else:
        thresh = XYZt / (XYZVt)
    
    return thresh, XYZt, XYZVt
    
# X, Y: yatayda dağın yayılımı
# Z: yükseklik (profil gibi düşün)
# Xv, Yv, Zv: yön vektörleri (küçük değişimler olabilir)

X  = [0, 2, 4, 6, 8]
Y  = [0, 1, 2, 3, 4]
Z  = [0, 2, 4, 6, 8]

Xv = [1, 1, 1, 1, 1]
Yv = [1, 1, 1, 1, 1]
Zv = [1, 1, 1, 1, 1]

Zp = 0

thresh_delta, shape_delta, vector_delta = m(X, Y, Z, Xv, Yv, Zv, Zp) 

print(f"Değişim eşiği: {thresh_delta}\nŞekil dağılım farkları: {shape_delta}\nYön dağılım farkları: {vector_delta}") 