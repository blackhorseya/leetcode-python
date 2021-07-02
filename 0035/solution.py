from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ret = 0

        for i, num in enumerate(nums):
            if num < target:
                ret = i + 1
            else:
                break

        return ret
