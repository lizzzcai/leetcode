'''
09/02/2020

1071. Greatest Common Divisor of Strings - Easy

Tag: String, GCD

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.


'''

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        Time: O(n^2) string match and slice
        Space: O(n^2)
        '''
        if not str1 or not str2:
            return str1 if not str2 else str2
        
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ""
        


# Solution
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        Time:o(n+m)
        Space:O(n+m)
        '''
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        d = gcd(len(str1), len(str2))
        return str1[:d] if str1[:d] * (len(str2) // d) == str2 and \
                str2[:d] * (len(str1) // d) == str1 else ""


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().gcdOfStrings
        self.assertEqual(func("ABCABC", "ABC"), "ABC")
        self.assertEqual(func("ABABAB", "AB"), "AB")
        self.assertEqual(func("LEET", "CODE"), "")

        func = Solution2().gcdOfStrings
        self.assertEqual(func("ABCABC", "ABC"), "ABC")
        self.assertEqual(func("ABABAB", "AB"), "AB")
        self.assertEqual(func("LEET", "CODE"), "")

if __name__ == '__main__':
    unittest.main()