def cutting(price,n):
    if(n>0):
        max_cost=0
        for i in range(n):
            max_cost=max(max_cost,price[i]+cutting(price,n-i-1))
        return max_cost
    else:
        return 0

l=list(map(int,input("enter the prices in consecutive manner :\t").split()))
n=int(input("enter the rod length : \t"))
print(f"maximum cost : {cutting(l,n)}")
