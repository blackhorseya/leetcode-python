from dataclasses import dataclass
from unittest import TestCase
import solution


class Test(TestCase):
    def setUp(self) -> None:
        self.s = solution.Solution()

    def test_solution(self):
        @dataclass
        class Args:
            x: int

        @dataclass
        class Testcase:
            name: str
            args: Args
            want: bool

        testcases = [
            Testcase(name="-121 then false", args=Args(x=-121), want=False),
            Testcase(name="8 then true", args=Args(x=8), want=True),
            Testcase(name="121 then true", args=Args(x=121), want=True),
            Testcase(name="10 then false", args=Args(x=10), want=False),
        ]

        for case in testcases:
            got = self.s.isPalindrome(case.args.x)
            self.assertEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
