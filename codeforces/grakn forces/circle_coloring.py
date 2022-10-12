t=int(input())
for _ in range(t):
    n=int(input())
    a=set()
    for i in range(3):
        b=list(map(int,input().split()))
        for j in b:            
            a.add(j)
    k=list(a)
    if(n % len(k)!= 1):
        for i in range(n):
            print(k[i % len(k)],end=" ")
    else:
        for i in range(n-1):
            print(k[(i) % len(k)],end=" ")
        print(k[1])
    print()        
        
