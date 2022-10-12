#Given a string S and a text T .find the shortest window which contains all the letters of T in s.
from collections import Counter

s,t=input("enter the string and text by leaving a space ").split()
txt=Counter(t)
min=len(s)
result=""
for i in range(len(s)):
	#print("in first loop")
	if(s[i] in txt):
		#print("in first")
		temp=txt.copy()
		k=""
		for j in range(i,len(s)):
			#print("in second loop") in this loop if the count of a single character is more than 1 after each time it is found we decrease its value by 1.
			if(s[j] in temp): 
				if(temp[s[j]]>1):
					temp[s[j]]-=1
					#print("in second")
				else:
					temp.pop(s[j])
					#print("in third") the element is removed from the dict 
				if(len(temp)== 0):
					k=s[i:j+1]
					#print("in fourth")
					if(min > len(k)):
						min=len(k)
						result=k
						#print("in last")
print(result)	
				