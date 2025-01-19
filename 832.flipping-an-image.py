#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result =[]
        for inner_list in image:
            n= len(inner_list)
            inner_list.reverse() # printing increases the runtim and gives bad results
            
            # # this commented section below is for inverting the numbers inplace for image
            # for idx in range(n):
            #     inner_list[idx]= int(not inner_list[idx])

            ## another method for solving the inversion 
            # for idx in range(n):
            #     inner_list[idx]= int(not inner_list[idx])
            # return image

            result.append([x ^ 1 for x in inner_list])



        return result
# @lc code=end

