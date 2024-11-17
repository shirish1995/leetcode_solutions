#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            # Choose between starting new subarray or continuing the existing one
            current_sum = max(num, current_sum + num)
            # Update maximum sum if current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum
# @lc code=end

