# sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi

import math
x=400
print(math.sqrt(x))

# pow(x,y) - x ning y-darajasini qaytaradi

print(pow(5,5))


# pi-π ning qiymatini saqlovchi o'zgaruvchi

from math import pi 
print(pi)

import random as r

son = r.randint(0,100)
print(son)


ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) 
print(ism)
print(r.choice(ism)) 


x = list(range(0,51,5))
print(x)
print(r.choice(x))


x = list(range(11))
print(x)
r.shuffle(x)
print(x)