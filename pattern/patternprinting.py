#displaying a diamond of length n with a character C
n=int(input())
c=input()
for i in range(1,n+1,2):
    print((c*i).center(n))
for i in range(n-2,0,-2):
    print((c*i).center(n))