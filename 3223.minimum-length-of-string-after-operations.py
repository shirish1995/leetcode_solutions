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
        saved_vals = []     
        deleteable_values= []
        deleteable_val_quantity= []
        for idx,val in enumerate(s):
            saved_vals.append(val)
        # print(saved_vals)    
        res = Counter(saved_vals)
        # print(res)
        # ressults= res[:]>2
        for results in res:
            if res[results]>2:
                deleteable_values.append(results)
                deleteable_val_quantity.append(res[results])
                
        if len(deleteable_values)==0:
            # print(len(saved_vals))
            return len(saved_vals)
        else:
            for i in range(len(deleteable_values)):
                # print("thisis the length of bthe deleteable values",(len(deleteable_values)-1)) #first pass gets me here
                # print("this is the current index",i) # first pass gets me idx=0
                # print("charecter in view/delete",deleteable_values[i]) #first char is "a"
                # print("number of the charecters that can be deleted",deleteable_val_quantity[i])
                

                # print("the amount of times the value can be deleted",deleteable_val_quantity[i]-1)
                # print(saved_vals)
                # print("length of str before deleting",len(saved_vals))
                if deleteable_val_quantity[i]%2==0: 
                    for j in range(deleteable_val_quantity[i]-2):
                        saved_vals.remove(deleteable_values[i])
                else:
                    for j in range(deleteable_val_quantity[i]-1):
                        saved_vals.remove(deleteable_values[i])
                
                # print(saved_vals)
                # print("the amount of times the value was deleted",deleteable_val_quantity[i]-1)
                # print("length of str after deleting",len(saved_vals))    
                # print("this is the length of the new input str",len(saved_vals))
            
                # if i ==len(deleteable_values)-2:
                #     print("this is the number of charecters that can be deleted from the else part", deleteable_val_quantity[i]-1 )
                #     return (len(saved_vals)-(deleteable_val_quantity[i]-1))
            return len(saved_vals)  
# @lc code=end

