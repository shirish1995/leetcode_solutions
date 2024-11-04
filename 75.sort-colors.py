#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
    
    # Optimization flag to detect if numsay is already sorted
        for i in range(n):
            # Flag to optimize when numsay is already sorted
            swapped = False
            
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # Compare adjacent elements
                if nums[j] > nums[j+1]:
                    # Swap them if they are in wrong order
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
                    
            # If no swapping occurred, numsay is already sorted
            if not swapped:
                break

# @lc code=end

