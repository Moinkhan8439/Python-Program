'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
 

Constraints:

-231 <= num <= 231 - 1
'''


class Solution:
    hexa="0123456789abcdef"
    def toHex(self, num: int) -> str:
        i=0
        res=""
        while(i<32):
            print(f'{num:064b} : num = {num}')
            n=num & 15                # Here we are taking the last 4 bit and doing AND with 1111
            res=self.hexa[n] + res
            num=num >> 4
            i=i+4                   # for bits movement
        return res[:-1].strip('0') + res[-1]


    
if __name__ == "__main__":
    s=int(input())
    x=Solution.toHex(Solution,s)
    print(x)
        

