'''
441. Arranging Coins
Easy

2776

1123

Add to List

Share
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
'''

'''
SOLUTION USING EQUATION FOR SUM OF N nUMBERS I.E n(n+1)//2=sum


2sum=n^2 + n 
2sum + (1/2)^2 = n^2 + 2*n*(1/2) + (1/2)^2 
solve it further


'''

from cmath import sqrt


class Solution:
    def arrangeCoins(self, s: int) -> int:
        return int(sqrt(2*s + 0.25) - 0.5)

s=int(input())
print(Solution.arrangeCoins(Solution,s))