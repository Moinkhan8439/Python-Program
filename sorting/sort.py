def partition(a,low,high):
    i=low-1
    pivot=a[high]
    print(a,end=" \t")
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


def asccheck(a):
    m=len(a)
    for i in range(m-1):
        if(a[i+1]< a[i]):
            return False
    return True

l=list(map(int,input("enter the number you wants to sort:\t").split()))
quicksort(l,0,len(l)-1)
print(f'after sorting : {l}')

