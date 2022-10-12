# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,n=input().split()
print(*["".join(b) for i in range(1,int(n)+1) for b in combinations(sorted(s),i)],sep="\n")
