'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest=2**(64)-1
        n=len(nums)
        nums.sort()
        res=closest
        for i in range(n-2):
            j,k=i+1,n-1
            while(j<k):
                sm=nums[i] + nums[j] + nums[k]
                # print(f'i={nums[i]} + j={nums[j]} + k={nums[k]} = {sm-abs(target)} < {closest}')
                if(abs(sm-target) < abs(closest-target)):
                    closest=sm
                if(sm > target):
                    k-=1
                else:
                    j+=1
        return closest



if __name__ == "__main__":
    l=list(map(int,input().split()))
    t=int(input())
    x=Solution.threeSumClosest(Solution,l,t)
    print(x)