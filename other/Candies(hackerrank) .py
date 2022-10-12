n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
res=[1]*n
for i in range(1,n):
	if(l[i] > l[i-1]):
		res[i]=res[i-1]+1
for i in range(n-1,0,-1):
	if(l[i-1] > l[i]):
		if(res[i-1] <= res[i]):
			res[i-1]=res[i]+1
print(sum(res,0))