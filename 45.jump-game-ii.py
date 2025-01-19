#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        number_of_jumps = 0
        last_item_in_list = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                number_of_jumps += 1
                break
            if i == last_item_in_list:      # Visited all the items on the current level
                number_of_jumps += 1        # Increment the level
                last_item_in_list = farthest  # Make the queue size for the next level

        return number_of_jumps
# @lc code=end

