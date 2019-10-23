import math
import random

print(math.pi, math.log10(2), math.sqrt(5))
print(complex(-1) ** 0.5)
r1 = []
for i in range(0,10):
    r1.append(random.randint(1, 500))

print(r1)

l2 = ['7-11','Fami','Hi-Life','bank']
print(random.choice(l2))

l3 = ['A','K','Q','J','10']
print(l3)
for i in range(0,10):
    random.shuffle(l3)
    print(l3)