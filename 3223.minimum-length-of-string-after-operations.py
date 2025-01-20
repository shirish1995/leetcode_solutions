#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        # saves count for all values in the current s (input) in "res"
        res = Counter(s)
        sum=0
        for results in res:
            if res[results]%2 ==0:
                res[results]=2
            else:
                res[results]=1
            sum= sum+res[results]
        return sum
# @lc code=end

