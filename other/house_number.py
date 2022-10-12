def digits(x):
    c=0
    while(x>0):
        x//=10
        c+=1
    return c

n=int(input())
dig=digits(n)
print(f"digit : {dig}")
count=0 
if(dig>2):
    count+=191+(n-pow(10,dig-1)+1)*dig
    for i in range(3,dig):
        count+=i*pow(10,i-1)
else:
    count=(n-9)*2+9

print(count)