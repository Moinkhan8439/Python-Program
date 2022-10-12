import time
def palindromeIndex(s):
    if(s!=s[::-1]):
        for i in range(len(s)):
            sub=s[:i]+s[i+1:]
            rev=sub[::-1]
            if(sub==rev):
                return(i)
    else:
        return -1

start=time.time()   
f=open("samplecase.txt")
data=f.read()
print(palindromeIndex(data))
f.close()
end=time.time()
print(end-start)