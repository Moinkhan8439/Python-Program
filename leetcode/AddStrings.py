'''Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if(len(num1) > len(num2)):
            num2=num2.zfill(len(num1))
        else:
            num1=num1.zfill(len(num2))
        carry=0
        res=""
        for i in range(len(num1)-1,-1,-1):            
            temp=int(num1[i])+int(num2[i])+carry            
            if temp > 9:
                carry=temp // 10
                temp=temp%10         
            else:
                carry=0
            res=str(temp)+res
        if(carry):
            res=str(carry)+res
        return res

s1=input()
s2=input()
print(Solution.addStrings(Solution,s1,s2))

