#monte carlo simualation methods .
#this method is considering that the circle is inscribed in the square..

import random
import decimal

sq=0
cir=0
N=1000
for i in range(N):
  x=random.uniform(0,1)
  y=random.uniform(0,1)
  if(x**2 + y**2<= 1):
    cir+=1
  else:
    sq+=1
pi=4*(cir/1000)
percentpi=round(abs(22/7-pi)*100/(22/7),2)
print(f"the approximated value of pi is {pi} i.e the error is {percentpi}%")

