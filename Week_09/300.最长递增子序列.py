#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# 1. DP，由于只问最长递增子序列的长度，可以表示当前状态dp[i]（到nums[i]的最长递增子序列的长度）
# dp方程
# 由于子序列可以不连续，所以用一次遍历是不对的，还要第二个下标j(j<i)
# 时间复杂度O(n^2)

# 2. 贪心+二分查找
# 新建一个tail列表，尾部总是最小的值
# tail[i]长度为i+1的所有上升子序列的结尾的最小值
# @lc code=start
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if len(nums) < 2:
        #     return len(nums)

        # dp = [1 for _ in range(len(nums))]

        # for i in range(1, len(nums)):
        #     # 遍历i之前的序列，如果nums[i] > nums[j]说明nums[i]可以追加在nums[j]后
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1, dp[i]) 
        # return max(dp)

        if len(nums) < 2: return len(nums)
        tails = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
                continue
            left = 0
            right = len(tails) - 1
            while left < right:
                mid = (left + right) >> 1
                if tails[mid] < nums[i]:
                    # mid一定不是要找的数， 因为tails[mid] < nums[i]
                    left = mid + 1
                else:
                    right = mid
            # 开头判断了nums[i] > tails[-1]的情况，所以这里一定能找到第 1 个大于等于 nums[i] 的元素
            tails[left] = nums[i]
        return len(tails)
# @lc code=end
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
