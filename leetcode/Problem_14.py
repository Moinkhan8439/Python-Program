'''14. Longest Common Prefix
Easy

10942

3477

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


class Solution:
    def longestCommonPrefix(self, strs:str) -> str:
        m = min(strs)
        strs[strs.index(m)] = strs[0]
        strs[0] = m
        c = strs[0]
        for i in range(1, len(strs)):
            for j in range(0, len(c)):
                if j < len(strs[i]):
                    if strs[i][j] != c[j]:
                        c = strs[i][:j]
                        break
                else:
                    c = strs[i][:j]
                    break
        return c


l=input()
x=Solution.longestCommonPrefix(Solution,l)
print(x)