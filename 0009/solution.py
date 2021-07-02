class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev, i = 0, x
        while i != 0:
            rev = rev * 10 + i % 10
            i = i // 10

        return x == rev
