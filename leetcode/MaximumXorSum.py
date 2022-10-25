'''
421. Maximum XOR of Two Numbers in an Array
Medium

4497

343

Add to List

Share
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
'''


class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        #O(n*n)
        # m=0
        # for i in nums:
        #     for j in nums:  
        #         m=max(m,i^j)
        # return m
        cmax = 0
        for i in range(31, -1, -1):
            tmp = cmax | (1 << i)
            S = set(tmp & j for j in nums)
            if any(j ^ tmp in S for j in S): 
                cmax = tmp
        return cmax


l=list(map(int,input().split()))
print(Solution.findMaximumXOR(Solution,l))