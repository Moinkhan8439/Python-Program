'''
448. Find All Numbers Disappeared in an Array
Easy

7549

411

Add to List

Share
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        misses=list()
        numSet=set(nums)
        for i in range(1,len(nums)+1):
            if i not in numSet:
                misses.append(i)
        return misses

l=list(map(int,input().split()))
x=Solution.findDisappearedNumbers(Solution,l)
print(x)