a=list(map(int,input("enter the array").split()))
n=len(a)
for i in range(n):
    min=a[i]
    index=i
    flag=True
    for j in range(i+1,n):
        if(a[j]<min):
            min=a[j]
            index=j
            flag=False
    a[i],a[index]=a[index],a[i]
    if(flag):
        break
    print(a)

