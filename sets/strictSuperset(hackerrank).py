'''
Sample Input 0

a=1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
b[0]=1 2 3 4 5
b[1]=1100 11 12
Sample Output 0

False
Explanation 0

Set b[0] is the strict superset of the set a but not of the set becauseb[1]  is not in set .
Hence, the output is False.
'''

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))