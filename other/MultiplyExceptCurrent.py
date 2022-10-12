#to take an array of integers and output another array which gives the mutliplication of all the elements from input array except the current position.eg- input=[1,2,3 4]
#   output =[24,12,8,6]

n=int(input())
l=[]
t=1
for i in range(n):
	k=int(input())
	l.append(k)
	t=t*k
res=[]
for i in l:
	res.append(t//i)
print(res)