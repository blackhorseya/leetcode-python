from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]

            if target == val:
                return mid
            elif target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1

        return left
