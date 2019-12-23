'''
22/12/2019

929. Unique Email Addresses - Easy

Tag: String

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

'''

from typing import List
# Solution
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        # a set to store unique email address
        res = set()
        for email in emails:
            local, domain = email.split("@")
            new_local_name = ""
            for char in local:
                # ignored everything after the first plus sign
                if char == "+":
                    break
                # ignore periods
                if char != ".":
                    new_local_name += char
            # create processed email address and add it into result set
            new_email = f"{new_local_name}@{domain}"
            res.add(new_email)

        return len(res)
                

# Unit Test
import unittest
class numUniqueEmailsCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numUniqueEmailsCase(self):
        func = Solution().numUniqueEmails
        self.assertEqual(func(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]), 2)

if __name__ == '__main__':
    unittest.main()