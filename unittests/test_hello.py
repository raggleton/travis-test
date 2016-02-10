"""A test...test"""


import sys
import unittest


class Simple_Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(1 + 2, 4)


def main():
    x = unittest.main()
    return x


if __name__ == '__main__':
    sys.exit(main())
