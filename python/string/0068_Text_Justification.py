'''
13/06/2020

68. Text Justification - hard

Tag: String

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(N*maxwidth^2)
    Space complexity : O(N*maxwidth)
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr, n_letters = [], [], 0
        for word in words:
            # len(curr): number of single space to be added, when adding the third word, we need two spaces, and curr has two word 
            # if exceed the max length, we start to process the line
            if len(curr) + n_letters + len(word) > maxWidth:
                space_to_add = maxWidth - n_letters
                i = 0
                while space_to_add>0:
                    # len(curr)-1 or 1: if only single word in curr, then will add space after it
                    curr[i%(len(curr)-1 or 1)] += " "
                    space_to_add -= 1
                    i += 1
                res.append(''.join(curr))
 
                # init for next line
                curr = []
                n_letters = 0
            
            curr.append(word)
            n_letters += len(word)
        
        if curr:
            res.append(' '.join(curr) + ' '*(maxWidth - n_letters - len(curr)+1))
        return res
        
        
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.fullJustify
            self.assertEqual(func(["This", "is", "an", "example", "of", "text", "justification."], 16), ["This    is    an","example  of text","justification.  "])
            
if __name__ == '__main__':
    unittest.main()