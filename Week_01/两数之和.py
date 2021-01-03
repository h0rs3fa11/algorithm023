
from typing import List

"""
解法1: 双指针夹逼；先排序，首尾各一个指针，计算两数之和，大于target说明需要缩小值，右边指针左移，小于说明要增加值，左边指针右移，找出最后的解；O(n)
解法2: 哈希表；建立一个哈希表，遍历nums，查找哈希表中是否有target-i的key，如果有即是解，没有就将i存入哈希表。O(n)
另：暴力O(n^2)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 解法1
        # # 由于要返回索引，所以不能直接在原列表上做排序
        # nums_tmp = nums.copy()
        # nums_tmp.sort()

        # i, j = 0, len(nums) - 1
        # while j > i:
        #     two_sum = nums[i] + nums[j]
        #     if two_sum == target:
        #         # 获取索引
        #         l = nums.index(nums_tmp[i])
        #         # 从nums中删除l索引的元素
        #         nums.pop(l)
        #         # 获取另一个元素的索引
        #         r = nums.index(nums_tmp[j])
        #         # 如果r的值大于或等于l，说明r索引的元素在l后面，因为nums删除了nums[l], l索引后的元素都左移了1，所以r要+1
        #         if r >= l:
        #             r += 1
        #         return [l, r]
        #     if two_sum > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return []

        # 解法2
        m = {}
        for i in range(len(nums)):
            a = m.get(target - nums[i])
            if a is None:
                m[nums[i]] = i
            else:
                return [a, i]
        return []

s = Solution()
print(s.twoSum([11,7,2,15], 14))