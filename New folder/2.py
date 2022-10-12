s=input().split()
d=dict()
for i in s:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
dup=list()
for i in d:
    if(d[i]>1):
        dup.append(i)
vowels={'a','e','i','o','u','A','E','I','O','U'}
for i in dup:
    lastv=0
    flag=True
    for j in i:
        if(j in vowels):
            ij=ord(j)-32 if(ord(j)>96) else ord(j)
            if(ij > lastv):
                lastv=ij     
            else:
                flag=False
                break
    if(flag==True):
        print(f'{i} {d[i]}',end=' ')