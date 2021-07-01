class Solution:
    def reverse(self, x: int) -> int:
        sig = 1
        val = x
        ret = 0

        if val < 0:
            sig = -1
            val = 0 - x

        while val > 0:
            ret = ret * 10 + val % 10
            val = val // 10

        if ret >= 1 << 31:
            return 0

        return ret * sig
