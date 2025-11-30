#dereceli kökler (python) 


"""modül olmadan"""
"""4. dereceden kök 8"""
n = 8
m = 4

kök = n ** (1/m) 

print(kök) 

"""modül kullanarak"""
"""4. dereceden kök 8"""
import math

kök = math.pow(n, 1/m) 

print(kök)  