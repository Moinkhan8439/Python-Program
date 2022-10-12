from operator import itemgetter
marksheet=[]
score=[]
for _ in range(int(input())):
	n=input()
	s=float(input())
	score.append(s)
	marksheet.append([n,s])
[print(a) for a,b in sorted(marksheet) if b==sorted(set(score))[1]]
	