'''
459. Repeated Substring Pattern
Easy

3901

357

Add to List

Share
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            sub=s[:i]
            if len(s) % len(sub) == 0 and sub * (len(s)//len(sub)) == s:
                return True
        return False


l=input()
print(l*10)
x=Solution.repeatedSubstringPattern(Solution,l)
print(x)     