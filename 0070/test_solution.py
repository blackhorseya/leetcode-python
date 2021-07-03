from dataclasses import dataclass
from unittest import TestCase
import solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = solution.Solution()

    def test_climb_stairs(self):
        @dataclass
        class Args:
            n: int

        @dataclass
        class Testcase:
            name: str
            args: Args
            want: int

        testcases = [
            Testcase(name="2 then 2", args=Args(n=2), want=2),
            Testcase(name="3 then 3", args=Args(n=3), want=3),
        ]

        for case in testcases:
            got = self.s.climbStairs(case.args.n)
            self.assertEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
