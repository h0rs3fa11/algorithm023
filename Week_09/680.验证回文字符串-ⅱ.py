#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        is_palindrome = lambda x : x == x[::-1]
        low, high = 0, len(s) - 1
        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return is_palindrome(s[low+1:high+1]) or is_palindrome(s[low:high])
        return True
        
# @lc code=end

