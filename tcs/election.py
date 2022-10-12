def showPos(s):
    apos=[]
    bpos=[]
    for i in range(0,len(s)):
        if(s[i]=="A"):
            apos.append(i)
        elif(s[i]=='B'):
            bpos.append(i)
    return apos,bpos
def acheck(i,bpos,s):
    if(i-1== -1 or s[i-1] !='-'):
        return False
    else:
        for j in bpos:
            if (j+1 == i-1):
                return False
    return True
def bcheck(i,apos,s):
    if(i+1== len(s) or s[i+1] !='-'):
        return False
    else:
        for j in apos:
            if (j-1 == i+1):
                return False
    return True

n=int(input())
s=input().split()
apos,bpos=showPos(s)
print(apos,bpos)
while(len(apos)!=0 and len(bpos) !=0):
    for i in range(0,len(apos)):
        if(acheck(apos[i],bpos,s)):
            apos[i]-=1
            s[apos[i]]="A"
            print("test")
        else:
            apos.remove(apos[i])
    print(s,apos)        
    for i in range(0,len(bpos)):
        if(bcheck(bpos[i],apos,s)):
            print("test")
            bpos[i]+=1
            s[bpos[i]]="B"        
        else:
            bpos.remove(bpos[i])
print(s)