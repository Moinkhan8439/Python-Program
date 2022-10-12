n=int(input())
a=[]
for i  in range(n):
	a.append(int(input()))
print(a)
i=a[0]
j=a[1]
count=2
max=1
for x in range(2,n):
	if(a[x]==i or a[x]==j):
		count+=1
		if(count>max):
			max=count
	else:
		i=a[x-2]
		j=a[x-1]
		count=2
print(max)
