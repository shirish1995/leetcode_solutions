#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (67.56%)
# Likes:    1175
# Dislikes: 2942
# Total Accepted:    177.8K
# Total Submissions: 261.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# An image smoother is a filter of the size 3 x 3 that can be applied to each
# cell of an image by rounding down the average of the cell and the eight
# surrounding cells (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present, we do not
# consider it in the average (i.e., the average of the four cells in the red
# smoother).
# 
# Given an m x n integer matrix img representing the grayscale of an image,
# return the image after applying the smoother on each cell of it.
# 
# 
# Example 1:
# 
# 
# Input: img = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[0,0,0],[0,0,0],[0,0,0]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# Example 2:
# 
# 
# Input: img = [[100,200,100],[200,50,200],[100,200,100]]
# Output: [[137,141,137],[141,138,141],[137,141,137]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) =
# floor(137.5) = 137
# For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6)
# = floor(141.666667) = 141
# For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) =
# floor(138.888889) = 138
# 
# 
# 
# Constraints:
# 
# 
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255
# 
# 

# @lc code=start

import numpy as np
import cv2
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        ## code below works if allowed to use open cv and numpy
        img = np.array(img, dtype=np.float32)
        kernel = np.ones((3,3),np.float32)
        output = cv2.filter2D(img,-1,kernel, borderType=cv2.BORDER_CONSTANT)
        valid_counts = cv2.filter2D(np.ones_like(img), -1, kernel, borderType=cv2.BORDER_CONSTANT)
        # print("this is the number of idx's that are neighbours and also inside the img", valid_counts)
        output=  np.floor(output / valid_counts).astype(np.int32)

        ## section below does avg by dividing by 9 for all elemnts even when on the edge of the img
        # kernel = np.ones((3,3), np.float32)/9 
        # output = cv2.filter2D(src=img,ddepth=-1,kernel=kernel)
        # #flooring the output
        # # output = np.floor(output)
        # output = output.astype(np.int32) #the var_name.astype(np.int32) removes the decimal point an dkeeps the int value
        return output        
            
# @lc code=end

