import unittest
import limit

class TestLimit (unittest.TestCase):
    def test_limit(self):
        self.assertEqual(limit.limit([1, 2, 3, 4, 5], 3, 3),
                        [3])
        self.assertEqual(limit.limit([1, 2, 3, 4, 5], None, 3),
                        [3, 4, 5])
        self.assertEqual(limit.limit([1, 2, 3, 4, 5], 3, None), 
                        [1, 2, 3])
        

if __name__ == '__main__' :
    unittest.main()