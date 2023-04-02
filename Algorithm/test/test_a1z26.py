import unittest
from Algorithm import a1z26

class TestA1z26(unittest.TestCase):
    def test_incode(self):
        self.assertEqual(a1z26.incode("mahdi"), [11, -1, 6, 2, 7])

    def test_dicode(self):
        self.assertEqual(a1z26.dicode([-1, 10, 7]), "ali")


if __name__ == '__main__':
    unittest.main()
