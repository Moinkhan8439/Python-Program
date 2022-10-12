a=list(map(int,input("enter the array").split()))
n=len(a)
count=0
for i in range(1,n):
    flag=True
    for j in range(n-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            count+=1
            flag=False           
    print(a,f' total swap = {count}')
    if(flag):
        break