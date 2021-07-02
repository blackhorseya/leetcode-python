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
            want: int

        testcases = [
            Testcase(name="[1,3,5,6] 5 then 2", args=Args(nums=[1, 3, 5, 6], target=5), want=2),
            Testcase(name="[1,3,5,6] 2 then 1", args=Args(nums=[1, 3, 5, 6], target=2), want=1),
            Testcase(name="[1,3,5,6] 7 then 4", args=Args(nums=[1, 3, 5, 6], target=7), want=4),
            Testcase(name="[1,3,5,6] 0 then 0", args=Args(nums=[1, 3, 5, 6], target=0), want=0),
            Testcase(name="[1] 0 then 0", args=Args(nums=[1], target=0), want=0),
        ]

        for case in testcases:
            got = self.s.searchInsert(case.args.nums, case.args.target)
            self.assertEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
