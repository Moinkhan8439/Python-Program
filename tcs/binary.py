import math
from itertools import combinations

def findsubsets(s, n): 
    return list(combinations(s, n))

n=int(input())
a=list(map(int,input().split()))
mx=max(a)
maxl=math.ceil(math.log(mx,2))
res=[]
count=0
totalx=0
totaly=0
for i in a:
    b=bin(i)
    x=maxl-int(math.log(i,2)+1) + len([j for j in bin(i)[2:] if j=="0"])
    y=len([j for j in bin(i)[2:] if j=="1"])
    totalx+=x
    totaly+=y
    if(x==y):
        count+=1
    res.append((x,y))
if(totalx==totaly):
    count+=1
for i in range(2,len(res)):
    sub=findsubsets(res,i)
    for j in sub:
        if(j[0][0]+ j[1][0] ==j[0][1]+j[1][1]):
            count+=1
if count!=0:
    answer="0"*(maxl-int(math.log(count,2)+1)) + bin(count)[2:]
else:
    answer="0"*maxl
print(answer)
