from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag = 0
        for num in nums:
            if num != val:
                nums[flag] = num
                flag += 1

        return flag
