#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (59.60%)
# Likes:    4253
# Dislikes: 243
# Total Accepted:    268K
# Total Submissions: 449.6K
# Testcase Example:  '3'
#
# There is only one character 'A' on the screen of a notepad. You can perform
# one of two operations on this notepad for each step:
# 
# 
# Copy All: You can copy all the characters present on the screen (a partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# 
# 
# Given an integer n, return the minimum number of operations to get the
# character 'A' exactly n times on the screen.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#
from collections import deque

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
            
        """
        Use BFS to explore possible states, where each state is (screen_length, clipboard_length).
        
        n: Target number of 'A's needed on screen
            
        Returns:
            Minimum number(type int) of operations needed
        """
        # If n is 1, so no operations needed return 0 cuz the letter is already printed
        if n == 1:
            return 0
            
        # Queue will store tuples of (screen_length, clipboard_length, operations)
        queue = deque([(1, 0, 0)])  # Start with one 'A' on screen
        # Keep track of visited states to avoid cycles
        visited = set([(1, 0)])
        
        while queue:
            screen_len, clipboard_len, ops = queue.popleft()
            
            # Try Copy All operation
            if (screen_len, screen_len) not in visited:
                # Copy all characters to clipboard
                if screen_len == n:
                    return ops + 1
                queue.append((screen_len, screen_len, ops + 1))
                visited.add((screen_len, screen_len))
            
            # Try Paste operation (only if clipboard is not empty)
            if clipboard_len > 0:
                new_screen_len = screen_len + clipboard_len
                if new_screen_len == n:
                    return ops + 1
                if new_screen_len < n and (new_screen_len, clipboard_len) not in visited:
                    queue.append((new_screen_len, clipboard_len, ops + 1))
                    visited.add((new_screen_len, clipboard_len))
        
        return 0  # Should never reach here given constraints
# @lc code=end

