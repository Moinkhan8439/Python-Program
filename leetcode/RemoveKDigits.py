'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''

#  TIME OUT EXCEEDED AS IT IS O(N*K)
# 
# class Solution:
#     def removeKdigits(self, s: str,k: int) -> str:
#         if len(s)==k:
#             return '0'
#         for i in range(k):
#             # print("smallest num",s)
#             res=s
#             for i in range(len(s)):
#                 new_num=s[:i]+s[i+1:]
#                 # print(f"Comparison is {new_num} <= {s}")
#                 if(int(new_num) <= int(res)):
#                     res=new_num
#             s=res
#         return s.lstrip('0')

#Using stack and based on the condition that if prev digits is less than current we delete the prev in the stack


from cgitb import small


class Solution:
    def removeKdigits(self, s: str,k: int) -> str:
        if len(s)==k:
            return '0'
        smallest=[]
        for i in s:                
            while(smallest and i < smallest[-1]  and k > 0):
                    k-=1
                    smallest.pop()
            smallest.append(i)
            print(smallest)
        if k > 0:
            smallest=smallest[:-k]
        res=""
        for i in smallest:
            res+=i
        if(int(res)==0):
            return '0'
        return res.lstrip('0')





if __name__ == "__main__":
    s=input()
    k=int(input())
    x=Solution.removeKdigits(Solution,s,k)
    print(x)