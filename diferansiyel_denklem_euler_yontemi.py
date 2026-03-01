#diferansiyel denklem 

t0,y0 = 0,1
h = 0.1

for it in range(1,2+1): 
    y0x = y0+h*(t0+y0)

    y0 = y0x
    t0 += h

    print(f'y{it}: {y0}, t{it}: {t0}')

'''
İlk adımda:
y₁ = y₀ + h ⋅ (t₀ + y₀) = 1 + 0.1 ⋅ (0 + 1) = 1.1

İkinci adımda:
y₂ = y₁ + h ⋅ (t₁ + y₁) = 1.1 + 0.1 ⋅ (0.1 + 1.1) = 1.1 + 0.12 = 1.22
'''
