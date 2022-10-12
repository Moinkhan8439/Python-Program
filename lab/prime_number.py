n=int(input())
if(n < 2):
    print("Not Prime")
else:
    i = 2
    flag=True
    while (i * i <= n):
        if (n % i == 0):
            print("Not Prime")
            flag=False
        i+= 1
    if(flag):
        print("Prime")

