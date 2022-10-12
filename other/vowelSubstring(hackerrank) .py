"""
Given a string s="caberqiitefg" and a length of a substring k, find the substring which has the maximum no.of vowels in the string s.
input s="caberqiitefg"
k=5
output:
	erqii
note: in case of more than one substing having same no.of vowels print the one having lowest index.
"""
import time

(s,n)=(input(),int(input()))
start=time.time()
vowels=list("aeiou")
l=[]
count=0
for i in range(len(s)):
	if(s[i] in vowels):
		count+=1
	l.append(count)
mx=0
for i in range(len(s)-n+1):
	if(s[i] in vowels):
		m=l[i+(n-1)]-l[i]+1
	else:
		m=l[i+(n-1)]-l[i]	
	if(m > mx):
		mx=m
		res=s[i:i+n]
print(res)
end=time.time()
print(end-start)