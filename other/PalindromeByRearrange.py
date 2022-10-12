from collections import Counter
s=input()
result=[]
for i in s:
	if(i in result):
		result.remove(i)
	else:
		result.append(i)
if(len(s)%2==1 and len(result)==1 or len(s)%2==0 and len(result)==0):
	print("possible")
else:
	print("not possible")

