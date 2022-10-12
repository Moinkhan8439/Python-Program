def partition(a,low,high):
    i=low-1
    pivot=a[high]
    print(a[low:high+1],end=" \t")
    for j in range(low,high):
        if(a[j]<= pivot):
            i+=1
            a[i],a[j]=a[j],a[i]
    i+=1
    a[i],a[high]=a[high],a[i]
    print(f'when the pivot was : {pivot} \t',f'\t the partition is at index {i}',a)
    return i

def quicksort(a,low,high):
    if low < high:
        p=partition(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)

a=list(map(int,input("enter the array : ").split()))
n=len(a)
quicksort(a,0,n-1)
print(a)