#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# 暴力：还原（O(logN)这里也是二分） => 升序 => 二分
# 正解：二分查找
# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # 1. 暴力
        # ordered = nums.copy()
        # # (1)如果不是升序 找到转折点并还原
        # if nums[0] > nums[-1]:
        #     left, right = 0, len(nums) - 1
        #     while left < right:
        #         mid = (left + right) >> 1
        #         if nums[mid] > nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     ordered[:] = nums[left:] + nums[:left]
        # # (2)二分查找
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) >> 1
        #     if ordered[mid] == target:
        #         return nums.index(ordered[mid])
        #     elif ordered[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return -1

        # 2.直接二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            
            # 左半部分升序
            # <=用于mid和left重合的特殊情况，向右收敛
            if nums[left] <= nums[mid]:
                # target大于等于左边界或小于等于nums[mid]，说明target在left,mid内，向左收敛
                if nums[left] <= target <= nums[mid]: 
                    right = mid - 1
                # 否则向右收敛
                else:
                    left = mid + 1
            # 左半部分旋转
            else:
                # target在mid和right内
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# @lc code=end
print(Solution().search([3,1], 1))
