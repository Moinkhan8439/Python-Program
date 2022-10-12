#we get inputs as an array and target ,we have to check whether the array has any pair of element whose sum eqauls  to target.for eg-a[2,7,9,11]   target=9 we return 1 since 2+7= 9


import time

start=time.time()
l=input().strip().split()
#k=[]
#for i in l:
#	k.append(int(i))
k=[int(i) for i in l]
t=int(input())
flag=False
for i in k:
	if t-i in k:
		print(i,t-i)
		flag=True
		break
if flag==False:
	print("not present")
end=time.time()
print(end-start)