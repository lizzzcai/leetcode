"""
15/09/2019
116. Fraction to Recurring Decimal - Medium
Tag: Math

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        negative = ((numerator < 0) != (denominator < 0))
        sign = ''
        if negative:
            sign = '-'
        # convert to positive value
        numerator = abs(numerator)
        denominator = abs(denominator)
        # get the quotient adn reminder
        quotient, reminder = divmod(numerator, denominator)
        #print(f"quotient: {quotient}, reminder: {reminder}")
        res = [sign+str(quotient), '.']
        
        check = []
        while reminder not in check:
            check.append(reminder)
            quotient, reminder = divmod(reminder*10, denominator)
            #print(f"quotient: {quotient}, reminder: {reminder}")
            res.append(str(quotient))

        #print(res)
        #print(check)
        # find the first location of the repeated reminder
        idx = check.index(reminder)
        # insert parentheses to res
        res.insert(idx + 2, '(')
        res.append(')')
        # join as string
        res = ''.join(res)
        # remove the case that numerator can be divided by denominator without fraction, 0 will be repeated
        res = res.replace('(0)', '')
        # remove the '.' at the end if any
        res = res.rstrip('.')
        return res



# Unit Test
import unittest
class fractionToDecimalCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fractionToDecimal(self):
        func = Solution().fractionToDecimal
 
        self.assertEqual(func(1, 2), '0.5')
        self.assertEqual(func(2, 1), '2')
        self.assertEqual(func(2, 3), '0.(6)')
        self.assertEqual(func(0, -5), '0')
        self.assertEqual(func(0, 3), '0')






if __name__ == '__main__':
    unittest.main()


