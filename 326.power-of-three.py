#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power_of_three(k):
            if k == 1:
                return True    
            if(k%3==0):
                return power_of_three(k//3)                
            else:
                return False
        if n >0:
            return power_of_three(n)
        else :
            return Falses
            
# @lc code=end

