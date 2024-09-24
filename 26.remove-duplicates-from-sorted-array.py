#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        #for i in range(len(nums)):
        while i+1 in range(len(nums)):
            if nums[i] == nums[(i+1)]:
                #print("this is the length of the nums int array before removing the element")
                #print(len(nums))
                nums.remove(nums[i])
                #print("this is the length of the nums int array")
                #print(len(nums))
                continue
            else:
                i+=1
                continue
        return len(nums)
# @lc code=end

