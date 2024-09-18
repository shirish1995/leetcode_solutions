#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_of_list = len (nums)
        for index in range(length_of_list):
            for temp_index in range(index+1,length_of_list):
                if (nums[index] + nums[temp_index]) == target:
                    return [index,temp_index]
            
            

# @lc code=end

