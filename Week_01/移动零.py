from typing import List
"""
双指针
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while j < len(nums):
            # 只有这个情况要交换，交换后i,j都后移
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            # 找到0后，如果nums[j]也是0，j继续后移找到最近一个不为0的元素，i不变
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
                continue
            i += 1
            j += 1
        return nums
    
print(Solution().moveZeroes([1, 0]))