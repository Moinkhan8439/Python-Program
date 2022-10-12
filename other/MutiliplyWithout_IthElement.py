l=input().split()
k=[]
for i in l:
	k.append(int(i))
n=len(k)
a=[1]
b=[1]
res=[]
temp1=1
temp2=1
for i in range(1,n):
	temp1=temp1*k[i-1]
	a.append(temp1)
	temp2=temp2*k[n-i]
	b.append(temp2)
print(a,b)
for i in range(n):
	res.append(a[i]*b[n-(i+1)])
print(res)