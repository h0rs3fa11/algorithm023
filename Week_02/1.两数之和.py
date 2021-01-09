#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 1.暴力 O(n^2)
# 2. 夹逼
# 3.hash
# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力 超时
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         two_sum = nums[i] + nums[j]
        #         if two_sum == target:
        #             return [i, j]
        # return []

        # hash table
        # m = {}
        # for i in range(len(nums)):
        #     if m.get(target-nums[i]) is not None:
        #         return [m.get(target-nums[i]), i]
        #     m[nums[i]] = i
        # return []

        # 夹逼
        temp = nums.copy()
        temp.sort()

        i = 0
        j = len(nums) - 1

        while j > i:
            two_sum = temp[i] + temp[j]
            if two_sum == target:
                l = nums.index(temp[i])
                nums.pop(l)
                r = nums.index(temp[j])
                # 注意 如果r大于等于l，说明r索引的元素在l索引之后，当l被pop后，r比原本的位置向左移动了一位
                if r >= l:
                    r += 1
                return [l, r]
            elif two_sum > target:
                j -= 1
            else:
                i += 1
        return []


# @lc code=end
s = Solution()
print(s.twoSum([11,7,2,15], 13))
