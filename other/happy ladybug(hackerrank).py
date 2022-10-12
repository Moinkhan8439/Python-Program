from collections import Counter

def check(m,n):
    flag=True
    if(len(m)==1):
        flag=False
    elif(len(m)==2 and m[0]!=m[1]):
        flag=False
    else:
        for i in range(1,n-1):
            if(m[i]==m[i-1] or m[i]==m[i+1]):
                continue
            else:
                flag=False
                break
    if(m[n-1]!=m[n-2]):
        flag=False    
    return flag

for i in range(int(input())):
    n=int(input())
    flag=True
    m=input()
    count=Counter(m)
    if(count["_"]==0):
        flag=check(m,n)
    else:
        for i in count.keys():
            if(i != "_" and count[i]<=1):
                flag=False    
    if(flag):            
        print("YES")
    else:
        print("NO")  
