#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. O(n)
        m = {}
        for i in t:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        
        for i in s:
            if i not in m:
                return False
            m[i] -= 1
        
        if any(m.values()):
            return False
        return True

        # 2. Python collections Counter
        # from collections import Counter
        # return Counter(s) == Counter(t)
# @lc code=end

