n=int(input())
a=[int(input()) for _ in range(n)]
b=set([int(input()) for _ in range(n)])
[print("({},{})".format(i,10-i)) for i in a if(10-i in b)]


#in simplified form
#for eg - a=1,3,5,9  and b =2,5,7,8  then the last line does this .
#first it take 1 from a and checks if 10-1 is in bif found then it prints the pair like in the case where i=3 it checks if 10-3 i.e 7 is in b or not since 7 is in b so it prints the pair in the format  (i,10-i)

