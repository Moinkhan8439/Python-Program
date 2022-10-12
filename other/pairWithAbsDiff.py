nk=input().split()
n=int(nk[0])
k=int(nk[1])
l=list(map(int,input().split()))
a={}
count=0
for i in range(n):
	a[l[i]]=0
for i in a:
	if i+k in a:
		count+=1
print(count)