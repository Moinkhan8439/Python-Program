#Given a string find firat non repeating characeter.  foreg- abcab    output: c
from collections import Counter
s=input()
l=Counter(s)
for i in s:
	if(l[i]==1):
		print(i)
		break