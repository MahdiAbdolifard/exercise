import unittest
import remove_min
# from Algorithm.remove_min import remove_min


class TestRemoveMin(unittest.TestCase):
    def test_remove_min(self):
        self.assertEqual(remove_min([4, 5, 2, 8, -2]), ([4, 5, 2, 8], -2))

# class TestRemoveMin(unittest.TestCase):
#     def test_remove_min(self):
#         stack1 = [4, 6, 1, 8, 3, 6]
#         stack2, min_val = remove_min(stack1)
#         self.assertEqual(stack2, [4, 6, 8, 3, 6])
#         self.assertEqual(min_val, 1)


if __name__ == '__main__':
    unittest.main()