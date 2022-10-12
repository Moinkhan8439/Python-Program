#given n no.of participants and their scores in next line.find the score of the runner up i.e second last.
n=int(input())
l=set(map(int,input().split()))
t=max(l)
l.remove(t)
print(max(l))