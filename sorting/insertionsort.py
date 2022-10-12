a=list(map(int,input("enter the array").split()))
n=len(a)
count=0
for i in range(1,n):
    temp=a[i]
    j=i-1
    while(j!=-1 and temp<a[j]):
        a[j+1]=a[j]
        j=j-1
        count+=1
    a[j+1]=temp
    print(a,f'swaps={count}')