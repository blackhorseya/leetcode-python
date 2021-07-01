from dataclasses import dataclass
from unittest import TestCase
import solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = solution.Solution()

    def test_reverse(self):
        @dataclass
        class Args:
            x: int

        @dataclass
        class Testcase:
            name: str
            args: Args
            want: int

        testcases = [
            Testcase(name="123 then 321", args=Args(x=123), want=321),
            Testcase(name="-123 then -321", args=Args(x=-123), want=-321),
            Testcase(name="120 then 12", args=Args(x=120), want=21),
            Testcase(name="0 then 0", args=Args(x=0), want=0),
        ]

        for case in testcases:
            got = self.s.reverse(case.args.x)
            self.assertEqual(case.want, got, "name: {}, got: {}, expected: {}".format(case.name, got, case.want))
