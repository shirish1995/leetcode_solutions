#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s: str, i: int) -> tuple[str, int]:
        # Initialize result string and number
            result = ""
            num = 0
            
            while i < len(s):
                char = s[i]
                
                # Case 1: If current char is a digit #1  0
                if char.isdigit():
                    num = num *10 + int(char)
                
                # Case 2: If we encounter opening bracket
                elif char == '[':
                    # Recursive call to process the content inside brackets
                    inner_str, next_i = decode(s, i + 1)
                    # Multiply the inner string by number and reset num
                    result += num * inner_str
                    num = 0
                    i = next_i
                
                # Case 3: If we encounter closing bracket
                elif char == ']':
                    # Return current result and position
                    return result, i
                
                # Case 4: If we encounter a letter
                else:
                    result += char
                
                i += 1
                
            return result, i

        # Start the decoding process
        decoded_string, _ = decode(s, 0)
        return decoded_string

        
        # def tri_recursion(k):
        #     if(k!=length_ofstring):
        #         result = k+tri_recursion(k-1)
        #         print(result)
        #     else:
        #         result = 0
        #     return result

        

# @lc code=end

