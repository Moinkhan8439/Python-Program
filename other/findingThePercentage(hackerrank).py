def perc(dic,s):
	sum=0
	for i in dic[s]:
			sum+=float(i)
	return sum/3
score=[]
marksheet={}
for _ in range(int(input())):
	get=input().split()
	score=get[1:]
	marksheet[get[0]]=score
print("{:.2f}".format(perc(marksheet,input())))
