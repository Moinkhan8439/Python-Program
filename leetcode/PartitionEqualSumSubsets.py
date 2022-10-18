'''
416. Partition Equal Subset Sum
Medium

9084

151

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''





# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         s=sum(nums)
#         nums.sort()
#         subsetSum=0
#         i=0
#         j=len(nums)-1
#         if(j+1 > 2):
#             while(i<=j):
#                 print(f'subset {subsetSum} i={nums[i]} j={nums[j]}')
#                 if i == j:
#                     temp=subsetSum+nums[i]               
#                 else:
#                     temp=subsetSum+nums[i]+nums[j]
#                     itemp=subsetSum+nums[i]
#                     jtemp=subsetSum+nums[j]
#                 if s-temp == temp:
#                     return True
#                 elif s-temp > temp:
#                     subsetSum+=nums[j]
#                 elif s-jtemp > jtemp:
#                     subsetSum+=nums[i]
#                 i=i+1
#                 j=j-1
#         else:
#             if(j>0):
#                 return nums[i] == nums[j]
#         x=0
#         for i in nums:
#             x+=i
#             if x==s-x:
#                 return True            
#         return False

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        if sum(nums)%2: return 0
        
        st = set([0])
        
        for i in nums:
            print(f'new line with i={i} st={st}')
            for j in list(st):
                print(st,j)
                st.add(i + j)
                if i + j == sum(nums)//2:
                    return True
        return False

            


l=list(map(int,input().split()))
x=Solution.canPartition(Solution,l)
print(x)