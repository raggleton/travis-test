"""A test...test"""


import sys
import unittest
from amodule.aclass import Adder


class Simple_Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(1 + 2, 4)

    def test_adder(self):
        a = Adder()
        self.assertEqual(a.add(10, 20), 40)


def main():
    return unittest.main()


if __name__ == '__main__':
    sys.exit(main())
