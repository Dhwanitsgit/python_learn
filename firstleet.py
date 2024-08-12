import numpy as np
import random

"""ans = random.uniform(-5,99)

print(type(list))"""
#list =  np.arange(-5, 100, 0.30)
list = [1,2,3,4,5,6,7,8]
ans = 8
Pair_found = False

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] + list[j] == ans:

            print(f"Pair found: ({list[i]}, {list[j]})")
            Pair_found = True
        if not Pair_found:
            print("Pair not Found")
print(list)