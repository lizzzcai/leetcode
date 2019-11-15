'''
15/11/2019

96. Unique Binary Search Trees - Medium

Tag: DynamicProgramming

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Solution
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
        
        G(n) = F(1,n) + F(2,n) + .. + F(n,n)
        F(3,7) = G(2)*G(4)
        F(j,n) = G(j-1)*G(n-j) 1<=i<=n
        
        Time: 1+2..+n = n(n+1)/2 = O(n^2)
        Space: O(n)

        '''
        
        if n <= 1:
            return 1
        
        G=[0]*(n+1)
        G[0] = 1 # empty tree
        G[1] = 1 # as root
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        
        return G[n]
        
        
# Unit Test
import unittest
class numTreesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numTreesCase(self):
        func = Solution().numTrees
        self.assertEqual(func(0), 1)
        self.assertEqual(func(1), 1)
        self.assertEqual(func(2), 2)
        self.assertEqual(func(3), 5)




if __name__ == '__main__':
    unittest.main()