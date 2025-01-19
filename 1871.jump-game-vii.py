#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#
# https://leetcode.com/problems/jump-game-vii/description/
#
# algorithms
# Medium (24.98%)
# Likes:    1719
# Dislikes: 111
# Total Accepted:    52K
# Total Submissions: 206.6K
# Testcase Example:  '"011010"\n2\n3'
#
# You are given a 0-indexed binary string s and two integers minJump and
# maxJump. In the beginning, you are standing at index 0, which is equal to
# '0'. You can move from index i to index j if the following conditions are
# fulfilled:
# 
# 
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# 
# 
# Return true if you can reach index s.length - 1 in s, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# 
# 
# Example 2:
# 
# 
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
# 
# 
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        length_s = len(s)
        if s[-1] != "0":  # If the last position is not reachable
            return False

        queue = [0]  # BFS queue initialized with the starting index
        visited = set()  # Track visited indices to avoid revisits
        farthest = 0  # The farthest index we've processed

        while queue:
            current_idx = queue.pop(0)

            # Process the range of indices we can jump to
            start = max(current_idx + minJump, farthest + 1)
            end = min(current_idx + maxJump, length_s - 1)

            for i in range(start, end + 1):
                if s[i] == "0" and i not in visited:
                    if i == length_s - 1:  # If we reach the last index
                        return True
                    queue.append(i)
                    visited.add(i)

            # Update the farthest index processed
            farthest = max(farthest, end)

        return False        
# @lc code=end

