"""Given  sets of integers,  and , print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
a=set(map(int,input().split()))
input()
b=set(map(int,input().split()))
print(*sorted(a.symmetric_difference(b)),sep="\n")
