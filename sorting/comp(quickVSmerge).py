import time
import random

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

def merge(a,low,mid,high):
    print(f'changes in block : {a[low:high+1]} in array {a} ',end="\t")
    i=low  
    j=mid+1
    k=0
    b=[]
    while(i<=mid and j<=high):
        if(a[i] < a[j]):
            b.append(a[i])
            k+=1
            i+=1    
        else:
            b.append(a[j])
            k+=1
            j+=1
        
    while(i<=mid):
        b.append(a[i])
        k+=1
        i+=1

    while(j<=high):
        b.append(a[j])
        k+=1
        j+=1
    for m in range(len(b)):
        a[m+low]=b[m]
    print(f'after merge : {a} ')

def mergesort(a,low,high):
    if(low<high):
        m=((low+high)//2)
        mergesort(a,low,m)
        mergesort(a,m+1,high)
        merge(a,low,m,high)

def asccheck(a):
    m=len(a)
    for i in range(m-1):
        if(a[i+1]< a[i]):
            return False
    return True

l=[]
k=[]
limit=int(input("enter how many random integers you want : \t"))
for i in range(limit):
    x=random.randint(1,9000)
    l.append(x)
    k.append(x)
print(f'before quick sort : {l}')
start=time.time()
quicksort(l,0,len(l)-1)
mid=time.time()
print(f'after sort : {l}')
print(f'before merge sort : {k}')
mergesort(k,0,len(k)-1)
end=time.time()
qtime=round((mid-start),5)
mtime=round((end-mid),5)
print(f'after sort : {k}')
print(f'time taken by merge sort : {mtime}s vs quick sort : {qtime}')
