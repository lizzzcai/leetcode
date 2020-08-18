'''
18/08/2020

1103. Distribute Candies to People - Easy

Tag: Math

We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        ans = [0]*num_people
        nxt = [i for i in range(1, num_people+1)]
        while candies > 0:
            s = sum(nxt)
            if s > candies:
                # do it one by one
                for i, x in enumerate(nxt):
                    if x < candies:
                        ans[i] += x
                        candies -= x
                    else:
                        ans[i] += candies
                        candies = 0
                        break
            else:
                # do it by batch
                for i, x in enumerate(nxt):
                    ans[i] += x
                    candies -= x
                
            nxt = [x+num_people for x in nxt]
        
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.distributeCandies
            self.assertEqual(func(7, 4), [1,2,3,1])
            self.assertEqual(func(10, 3), [5,2,3])


if __name__ == '__main__':
    unittest.main()