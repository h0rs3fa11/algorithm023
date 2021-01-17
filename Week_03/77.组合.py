#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1. 比较好理解方法
        # # 生成数字列表
        # nums = [i for i in range(1, n+1)]
        # res = []
        # def backtrace(curr_res, index):
        #     # 结果长度已满足，加到结果集中
        #     if len(curr_res) == k:
        #         # 此处不用切片做拷贝，后面修改curr_res时会修改res里面的值
        #         res.append(curr_res[:])
        #         return
        #     # process and recursion
        #     for i in range(index, n):
        #         # 当前层的结果
        #         curr_res.append(nums[i])
        #         # 递归，传入当前层结果，开始索引+1避免重复
        #         backtrace(curr_res, i + 1)
        #         # pop最尾一个开始新的迭代，例如[1,2]，删掉2后[1]进行下一个3的处理==>[1,3]
        #         curr_res.pop()
        # # 特殊条件
        # if not (n and k):
        #     return res
        # # 初始结果集和索引
        # backtrace([], 0)
        # return res

        # python itertools库函数
        # return list(itertools.combinations(range(1, n+1), k))
# @lc code=end
Solution().combine(4, 2)
