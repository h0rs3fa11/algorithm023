# 前提 升序数组部分旋转后
# 转折点为k，左边界nums[left], 右边界nums[right]
# 旋转后 nums[right] < nums[left]
# k与nums[right]比较，如果大于，说明转折点还在后面（右边），向右收敛
# 否则说明刚到转折点或转折点在右边，向左收敛（right = mid）
# 最后返回left
def find_disorder(nums: list) -> int:
    left, right = 0, len(nums) - 1
    # 这种情况说明nums递增，没有被旋转
    if nums[right] > nums[0]:
        return -1
    
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

num = [6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5]
print(find_disorder(num))