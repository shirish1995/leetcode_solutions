#
# @lc app=leetcode id=2116 lang=python3
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution:
    # import re  # Import regex module
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        open_count = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                
                return False
            # print("open count",open_count)

        close_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
            # print("close count",close_count)

        return True

# s= "((()(()()))()((()()))))()((()(()"
# locked= "10111100100101001110100010001001"
# s= "(()(()()" # oc= 1+1+1(locked_0)+1+1-1+1=6 CC= -1-1+1(locked_0)-1+1(locked_0)+1+1(locked_0)
# locked= "11010101"
# @lc code=end

