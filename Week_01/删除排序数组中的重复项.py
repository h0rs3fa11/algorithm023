"""
解法1: 利用set类型没有重复元素的特性，将List转为set再转为list返回长度
解法2: 双指针
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # 解法1
        # # 需要原地修改，所以这里是nums[:]
        # # 由于原数组是排好序的，返回的顺序不能变，所以在set => list这一步还需要再排序
        # nums[:]  = list(sorted(set(nums)))
        # return len(nums)

        # 解法2
        slow, fast = 0, 1
        while fast < len(nums):
            # 如果nums[fast]等于nums[slow]，fast往后一位
            if nums[fast] == nums[slow]:
                fast += 1
            # 如果不相等，slow后移，nums[slow]的值改变为fast的值
            else:
                slow += 1
                nums[slow] = nums[fast]
        # 最后返回slow为最后一个元素的列表长度
        return slow + 1

test_nums = [1, 1, 2]
print(Solution().removeDuplicates(test_nums))