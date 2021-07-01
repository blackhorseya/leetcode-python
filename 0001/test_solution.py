from dataclasses import dataclass
from typing import List
from unittest import TestCase
import solution


class Test(TestCase):
    def setUp(self) -> None:
        self.s = solution.Solution()

    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]
            target: int

        @dataclass
        class Testcase:
            name: str
            args: Args
            want: List[int]

        testcases = [
            Testcase(name="[2,7,11,15] 9 then [0,1]", args=Args(nums=[2, 7, 11, 15], target=9), want=[0, 1]),
            Testcase(name="[3,2,4] 6 then [1,2]", args=Args(nums=[3, 2, 4], target=6), want=[1, 2]),
            Testcase(name="[3,3] 6 then [0,1]", args=Args(nums=[3, 3], target=6), want=[0, 1]),
        ]
        for case in testcases:
            got = self.s.twoSum(case.args.nums, case.args.target)
            self.assertListEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
