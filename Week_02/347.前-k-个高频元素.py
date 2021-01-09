#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 堆/Counter, Counter还可以直接用most_common函数
        # from collections import Counter
        # import heapq
        # counter = Counter(nums)
        # if len(list(counter.keys())) == 1: return [list(counter.keys())[0]]
        # hp = [-x for x in counter.values()]
        # max_k, res = [], []
        # heapq.heapify(hp)
        # for i in range(k):
        #     max_k.append(-heapq.heappop(hp))
        # for key, v in counter.items():
        #     if v in max_k:
        #         res.append(key)
        # return res[:k]

        # 排序
        from collections import Counter
        counter = Counter(nums)
        if len(list(counter.keys())) == 1: 
            return [list(counter.keys())[0]]
        res = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in res[:k]]
# @lc code=end
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))
