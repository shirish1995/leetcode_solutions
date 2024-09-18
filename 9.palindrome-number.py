#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            digits = [int(digit) for digit in str(x)]
            return digits == digits[::-1]
        else:
            return False
# @lc code=end

