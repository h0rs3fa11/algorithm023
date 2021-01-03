from typing import List
"""
题目要求空间复杂度O(1)
解法1: 暴力；遍历nums，每个元素与最后一个元素交换，这样一轮后相当于数组右移了一位；进行这样的操作k轮，相当于数组右移了k位
使用这种方法在leetcode提交会超时

解法2: 三次翻转；第一次旋转前n-k个元素，第二次旋转剩下的k个元素，最后整个数组旋转一次，得到结果
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # # 解法1
        # for _ in range(k):
        #     for i in range(len(nums)):
        #         nums[i], nums[-1] = nums[-1], nums[i]
        
        # 解法2
        n = len(nums)
        k = k % n
        # 旋转数组
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)