n=int(input())
mx=0
prevmax=0
prevwin=""
win=""
d=dict()
key=list()
score=list()
for i in range(n):
    s,sc=input().split()
    key.append(s)
    score.append(int(sc))
    if s in d:
       d[s]=int(sc)+d[s]
    else:
        d[s]=int(sc)
mx=max(d.values())
allmax=list()
for i,j in d.items():
    if(j==mx):
        allmax.append(i)
final=dict()
for i,j in zip(key,score):
    if i in final:
        final[i]+=j
    else:
        final[i]=j
    if(final[i] >= mx and i in allmax):
        win=i
        break
print(win)

