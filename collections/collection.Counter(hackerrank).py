from collections import Counter
n=int(input())
size=Counter(list(map(int,input().split())))
profit=0
for _ in range(int(input())):
    i,j=list(map(int,input().split()))
    if(i in size and size[i]!=0):
        size[i]-=1
        profit+=j
print(profit)