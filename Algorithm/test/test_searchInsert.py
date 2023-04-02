import unittest
from Algorithm import searchInsert

class TestSearchInsert(unittest.TestCase):

    def test_search_insert(self):
        self.assertEqual(searchInsert.search_insert([1, 3, 5, 6], 4), 2)
        self.assertEqual(searchInsert.search_insert([1, 3, 5, 6], 3), 1)

    def test_search_insert_2(self):
        self.assertEqual(searchInsert.search_insert_2([1, 3, 5, 6], 7), 4)
        self.assertEqual(searchInsert.search_insert_2([1, 3, 5, 6], 0), 0)


if __name__ == '__main__':
    unittest.main()
