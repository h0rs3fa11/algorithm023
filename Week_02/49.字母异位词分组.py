#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # 1. 排序数组分类
        # m = defaultdict(list)
        # for s in strs:
        #     m[tuple(sorted(s))].append(s)
        # return list(m.values())

        # 2. 字母个数分类
        # m = defaultdict(list)
        
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     m[tuple(count)].append(s)
        # return list(m.values())

        # 与1相同，使用python默认dict
        m = {}
        for s in strs:
            key = tuple(sorted(s))
            m[key] = m.get(key, []) + [s]
        return list(m.values())
# @lc code=end

