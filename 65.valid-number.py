#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start


import re


class Solution:
    def isNumber(self, s: str) -> bool:
        # allowed_characters = [".", "e", "E", "+", "-"]
        # # Check if string has characters that are not numbers and not any of the allowed_characters

        # if 
        #     return False
        # return True

        # 1. Typecast method
        # infinities = ("inf","+inf","-inf","Infinity","+Infinity","-Infinity", "nan")
        # try:
        #     res = float(s)
        #     if s in infinities:
        #         return False
        #     return True
        # except:
        #     return False
        
        # 2. Regex method
        expr = r"[+-]?\d*(\.)?\d*[eE]?[+-]?\d+"
        
        res = re.match(expr, s)
        if res:
            return True
        else:
            return False

# @lc code=end

