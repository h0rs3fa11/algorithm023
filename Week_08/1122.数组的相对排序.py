#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
from typing import List
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # # 自定义比较排序
        # # 出现在rank中的第一个元素为0会排在前面，rank是arr2中的索引和元素的映射，比较第二个元素rank[x]实际上就是比较在arr2中的元素的大小
        # def mycmp(x: int) -> (int, int):
        #     return rank[x] if x in rank else x
        # # rank={元素:arr2中的相对位置}
        # # i-len(arr2)一定是负数， 会排在前
        # rank = {x: i-len(arr2) for i, x in enumerate(arr2)}
        # arr1.sort(key=mycmp)
        # return arr1

        # 计数排序
        # 本题中元素的范围为 [0, 1000][0,1000]，这个范围不是很大，我们也可以考虑不基于比较的排序，例如「计数排序」。
        import collections
        counter = collections.Counter(arr1)
        ans = list()
        # 在arr2中的元素
        for x in arr2:
            ans.extend([x] * counter[x])
            counter[x] = 0
        # 不在arr2中的元素
        for x in range(1001):
            if counter[x] > 0:
                ans.extend([x] * counter[x])
        return ans
# @lc code=end

Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])