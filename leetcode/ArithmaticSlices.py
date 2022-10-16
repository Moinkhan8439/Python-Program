'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if(len(nums)<3):
            return 0
        diff=nums[1]-nums[0]
        start=0
        end=2
        c=0
        for i in range(2,len(nums)):
            currDiff=nums[i] -nums[i-1]
            if(currDiff != diff):
                size=end-start
                # print(f'end={end} and start={start}')
                c+=self.calculateSlices(size)
                start=i-1
            end=i+1   
            diff=currDiff
        # print(f'after loop end={end} and start={start}')
        if(end - start >= 3 ):
            # print(f'end={end} and start={start}')
            c=c+self.calculateSlices(end- start)       
        return c

    '''
    For size 3 slices are 1
    for size 4            3
    for size 5            6
    for size 6            10
     noow this sequence is n(n+1)/2 where n is size-2
    '''

    def calculateSlices(size):
        return (size-2)*(size-2+1)//2   



            


s=list(map(int,input().split()))
print(Solution.numberOfArithmeticSlices(Solution,s))