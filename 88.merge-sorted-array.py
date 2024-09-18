#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
import numpy as np
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = len(nums1)
        n = len(nums2)
        nums1 = []
        for count in range(m+n):
            for i in range(n):
                if count >= m:
                    nums1[count] = nums2[i]
                else:
                    continue


                    
        
# @lc code=end

