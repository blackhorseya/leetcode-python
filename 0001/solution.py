from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, num in enumerate(nums):
            want = target - num

            if m.get(want) is not None:
                return [m.get(want), i]

            m[num] = i

        return []
