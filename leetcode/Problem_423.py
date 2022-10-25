'''
423. Reconstruct Original Digits from English
Medium

684

2317

Add to List

Share
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
'''
from collections import Counter

class Solution:
    def originalDigits(self, s:str) -> str:
        d=Counter(s)
        count=[0]*10
        if 'z' in d:
            count[0]=d['z']
        if 'w' in d:
            count[2]=d['w']
        if 'u' in d:
            count[4]=d['u']
        if 'x' in d:
            count[6]=d['x']
        if 'g' in d:
            count[8]=d['g']
        count[1]=d['o'] - (count[0] + count[2] + count[4])
        count[3]=d['t'] - (count[2] + count[8])
        count[5]=d['f'] - (count[4])
        count[7]=d['s'] - (count[6])
        count[9]=d['i'] - (count[5] + count[6] + count[8]) 
        res=""
        for i in range(0,10):
            if count[i] != 0:
                res+=str(i)*count[i]
        return res


l=input()
x=Solution.originalDigits(Solution,l)
print(x)