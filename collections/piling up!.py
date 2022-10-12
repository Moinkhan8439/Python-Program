import math
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=True
    for i in range(1,math.ceil(n/2)):
        if(l[i]>l[i-1] or l[i]>l[0-i] or l[-1-i]>l[i-1] or l[-1-i]>l[0-i]):
            print("NO")
            flag=False
    if(flag==True):
        print("YES")