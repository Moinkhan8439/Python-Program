"""
You are given a complex z. Your task is to convert it to polar coordinates.
Sample Input

  1+2j
Sample Output

 2.23606797749979 
 1.1071487177940904
"""


import cmath

c=complex(input())
print(*cmath.polar(c),sep="\n")