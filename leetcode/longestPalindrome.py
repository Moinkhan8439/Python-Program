'''Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        b=Counter(s)
        c=0
        odd=False
        for i in b:
            if(b[i]&1):
                odd=True
                c+=b[i]-1
            else:
                c+=b[i]
        return c+1 if odd else c

s=input()
print(Solution.longestPalindrome(Solution,s))