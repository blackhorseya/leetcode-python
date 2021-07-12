from dataclasses import dataclass
from typing import List
from unittest import TestCase
import solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = solution.Solution()

    def test_remove_element(self):
        @dataclass
        class Args:
            nums: List[int]
            val: int

        @dataclass
        class Testcase:
            name: str
            args: Args
            want: int

        testcases = [
            Testcase(name="[3,2,2,3] 3 then 2", args=Args(nums=[3, 2, 2, 3], val=3), want=2),
            Testcase(name="[0,1,2,2,3,0,4,2] 2 then 5", args=Args(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2), want=5),
        ]

        for case in testcases:
            got = self.s.removeElement(case.args.nums, case.args.val)
            self.assertEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
