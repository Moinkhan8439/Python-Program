# Enter your code here. Read input from STDIN. Print output to STDOUT()
_=input().split()
arr=input().split()
x=set(input().split())
y=set(input().split())
total=0
for i in arr:
    if(i in x):
        total+=1
    elif(i in y):
        total-=1
print(total)
