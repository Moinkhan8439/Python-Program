
def ice(m,a):
	for i in range(len(a)):
		if m-a[i] in a:
			for j in range(i+1,len(a)):
				if(a[j]==m-a[i]):
					print(i+1,j+1)
					break
	

t=int(input())
for i in range(t):
	m=int(input())
	n=int(input())
	l=input().split()
	k=[]
	for i in l:
		k.append(int(i))
	ice(m,k)