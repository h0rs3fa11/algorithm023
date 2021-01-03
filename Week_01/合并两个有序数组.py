"""
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
要求在nums1原地修改
"""
from typing import List
"""
解法1: 直接合并后重新排序，O((n+m)log(n+m))
解法2: 双指针；将nums1的元素（前m个）保存到一个临时列表中，将临时列表nums1_tmp和nums2比较，把较小的元素放入nums1中。O(n+m)
解法3: 三指针；用三个指针，从后往前，1遍历nums1，2遍历nums2，3从nums1的最末尾（m+n-1）开始，比较nums1 nums2，较大的放入3。O(n+m)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # # 解法1
        # nums1[:] = sorted(nums1[:m] + nums2)

        # # 解法2
        # nums1_tmp = nums1[:m]
        # # 清除nums1
        # nums1[:] = []
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1_tmp[i] < nums2[j]:
        #         nums1.append(nums1_tmp[i])
        #         i += 1
        #     else:
        #         nums1.append(nums2[j])
        #         j += 1
        
        # # 循环结束后，可能有一方数组未遍历完，将其拼接到nums1后面
        # if i < m:
        #     nums1[i + j:] = nums1_tmp[i:]
        # if j < n:
        #     nums1[i + j:] = nums2[j:]

        # 解法3
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # 循环结束后，可能有一方数组未遍历完，如果是nums1未遍历完不需要进行其他操作，如果是nums2未遍历完，要把剩下的n个元素拷贝到nums1的前n个位置处。nums2剩下的元素是循环结束后的j值+1
        nums1[:j+1] = nums2[:j+1]
