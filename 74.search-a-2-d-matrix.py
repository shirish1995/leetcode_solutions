#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix = np.array(matrix)

        return (bool(np.any(matrix.flatten()== target)))
        
# @lc code=end

