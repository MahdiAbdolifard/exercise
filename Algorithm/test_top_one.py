import unittest
import top_one

class TestTop_one(unittest.TestCase):
    def tset_top_one(self):
        self.assertEqual(top_one.top_one([1, 2, 3, 2, 2, 3, 4, 5, 5, 5, 2, 2]), 
                        "The number 2 is the most repeated (5 times).")


if __name__ == '__main__' :
    unittest.main()
