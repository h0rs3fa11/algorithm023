from typing import List
"""
解法1: 递归；进位看作重复子问题，终止条件是当前digits的末尾元素digits[-1]小于9以及digit为None
解法2: 迭代
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # 解法1
        # if not digits:
        #     # 9，99，999 的情况
        #     return [1]
        # if digits[-1] != 9:
        #     # 不用进位，加1返回
        #     digits[-1] += 1
        #     return digits

        # # 需要进位，先把末尾置零
        # digits[-1] = 0
        # # digits[:-1]是除去末尾元素的其他元素，开始递归
        # d = self.plusOne(digits[:-1])
        # d.append(digits[-1])
        # return d

        # 解法2
        new = []
        # 当前末位是9
        while digits and digits[-1] == 9:
            # 删除多少个末位就在new中增加多少0
            digits.pop()
            new.append(0)

        # 只有9的情况
        if not digits:
            return [1] + new
        # 最后的进位
        digits[-1] += 1
        return digits + new