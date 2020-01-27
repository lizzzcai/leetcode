'''
27/01/2020

739. Daily Temperatures - Medium

Tag: Array

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

'''

from typing import List
# Solution
class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        Time Complexity: O(NW), where N is the length of T and W is the number of allowed values for T[i]. Since W = 71, we can consider this complexity O(N).

        Space Complexity: O(N+W), the size of the answer and the next array.

        check it by reverse order.
        for each tmp, check the [temp+1, 100] in tmp_idx by tmp_idx[tmp]
        find the min tmp_idx[tmp] if exist, ans[i] = min(warmer_idxs) - i
        update the idx of current tmp by tmp_idx[tmp] = i
        
        '''
        # init the result and tmp_idx arrays
        ans = [0] * len(T)
        tmp_idx = [None]*101
        
        # check by reverse order
        for i in range(len(T)-1, -1, -1):
            tmp = T[i]
            # find all the temp which > tmp and their idx
            warmer_idxs = [tmp_idx[j] for j in range(tmp+1, 101) if tmp_idx[j] != None]
            # if exist, update the it to answer
            if warmer_idxs:
                ans[i] = min(warmer_idxs) - i
            # update the idx of tmp
            tmp_idx[tmp] = i
        
        return ans
            
class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        
        Time Complexity: O(N), where N is the length of T and W is the number of allowed values for T[i]. Each index gets pushed and popped at most once from the stack.

        Space Complexity: O(W). The size of the stack is bounded as it represents strictly increasing temperatures.        
        
        '''
        ans = [0] * len(T)
        stack = []
        # keep a stack with i that T[i] decrese
        # T[stack[-1]]< T[stack[-2]] < ...
        # stack[-1] is the latest i close to T[]
        for i in range(len(T)-1, -1, -1):
            # find the next warmer occurs, pop the tmp lower than current
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            # if has, update ans
            if stack:
                ans[i] = stack[-1] - i
            # add the current to stack
            stack.append(i)
        return ans  

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().dailyTemperatures
        self.assertEqual(func([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
        self.assertEqual(func([89,62,70,58,47,47,46,76,100,70]), [8,1,5,4,3,2,1,1,0,0])

        func = Solution2().dailyTemperatures
        self.assertEqual(func([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
        self.assertEqual(func([89,62,70,58,47,47,46,76,100,70]), [8,1,5,4,3,2,1,1,0,0])

if __name__ == '__main__':
    unittest.main()