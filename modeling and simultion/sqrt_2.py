#monte carlo simualation methods .

import random
import decimal

N=1000
n=0
for i in range(N):
	x = random.uniform(0,2)
	if x**2 < 2:
		n+=1
		print(f"Randomnly generated value : {x}")

print(f"Approximatied square root of 5 : \t {N/n}")