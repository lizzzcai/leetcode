

def bubble_sort(arr):
    '''
    https://www.runoob.com/python3/python-bubble-sort.html
    O(n^2)

    stable
    '''
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr



# Unit Test
import unittest
class selection_sortCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_selection_sort(self):

        func = bubble_sort
        # test 1
        self.assertEqual(func([54,26,93,17,77,31,44,55,20]), [17, 20, 26, 31, 44, 54, 55, 77, 93])

        # test 2
        self.assertEqual(func([-99, -12, 3, -1000]), [-1000, -99, -12, 3])

        # test 3
        self.assertEqual(func([9,9,8,7,6,5,4,3,2,1,0]), [0,1,2,3,4,5,6,7,8,9,9])

        # test 4
        self.assertEqual(func([2]), [2])

        # test 5
        self.assertEqual(func([]), [])

if __name__ == '__main__':
    unittest.main()