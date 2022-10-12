import math

n=int(input())
k=int(input("enter the no. we dont want : "))
ndigit=math.ceil(math.log(n,10))-1
res=0
while(ndigit >= 0):
    temp=n//(10**ndigit)
    n-=temp*(10**ndigit)
    if( temp == k ):
        res+=(temp-1)*(10**ndigit)
        ndigit-=1
        break
    else:
        res+=temp*(10**ndigit)
        ndigit-=1
    print(f'ndigit = {ndigit}  res={res} n={n}' )
if(ndigit >= 0):
    if(k !=9):
        res+=(10**(ndigit+1)//9)*9
    else:
        res+=(10**(ndigit+1)//9)*8
print(res)
