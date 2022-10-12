def merge(a,low,mid,high):
    b=[]
    i=low
    j=mid+1
    #print(f'i={a[i]} j={a[j]} in a : {a} ')
    while(i<=mid and j<=high):
        if(a[i] < a[j]):
            b.append(a[i])
            i+=1
        elif(a[j]<a[i]):
            b.append(a[j])
            j+=1
        else:
            b.append(a[i])
            b.append(a[j])
            i,j=i+1,j+1
    while(i<=mid):
        b.append(a[i])
        i+=1
    while(j<=high):
        b.append(a[j])
        j+=1
    for i in range(len(b)):
        a[i+low]=b[i]

def mergesort(a,low,high):
    if(low<high):
        mid=(low+high)//2
        mergesort(a,low,mid)
        mergesort(a,mid+1,high)
        merge(a,low,mid,high)


a=list(map(int,input("enter the array : ").split()))
n=len(a)
mergesort(a,0,n-1)
print(a)