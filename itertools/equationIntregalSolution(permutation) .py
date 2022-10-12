from itertools import permutations

(n,k)=(int(input()),int(input()))
s="0123456789"
perm=list(permutations(s,n))
count=0
for i in perm:
	sum=0
	for j in range(n):
		sum+=int(i[j])
	if(sum==k):
		count+=1
		print(i)	
print(count)
	