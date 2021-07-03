class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        while n > 0:
            b = b + a
            a = b - a

            n = n - 1

        return a
