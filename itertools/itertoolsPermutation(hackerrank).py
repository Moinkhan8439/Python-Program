"""Print the permutations of the string  on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible size 2 permutations of the string HACK are printed in lexicographic sorted order."""
from itertools import permutations

def tr():
    return "\n"

a,n=input().split()
print(*[''.join(i) for i in permutations(sorted(a),int(n))],sep='\n',end='\n')

