n=int(input())
a=list(map(int,input().split()))
count=1
mx=1
for i in range(len(a)-1):
    if(a[i+1]>a[i]):
        count+=1
    else:
        if(mx < count):
            mx=count
            count=1
if(mx < count):
    mx=count
print(mx)