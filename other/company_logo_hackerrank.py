s = input()
m=dict()
for i in s:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
value=sorted(m.items(),key= lambda x:(-x[1],x[0]))
res=value[:3]
print(res) 



    