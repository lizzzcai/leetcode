'''
01/05/2020

648. Replace Words - Medium

Tag: Hash Table, Trie

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

 

Example 1:

Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Constraints:

The input will only have lower-case letters.
1 <= dict.length <= 1000
1 <= dict[i].length <= 100
1 <= sentence words number <= 1000
1 <= sentence words length <= 1000

'''

from typing import List
# Solution
class Tire:
    def __init__(self):
        self.next = {}
        
    def insert_root(self, word):
        nodes = self.next
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        
        nodes['#'] = True
    
    def find_root(self, word):
        nodes = self.next
        for idx, ch in enumerate(word):
            if ch not in nodes:
                return word
            nodes = nodes[ch]
            if '#' in nodes:
                return word[:idx+1]
        return word
            
            


class Solution1:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        
        tire = Tire()
        for root in dict:
            tire.insert_root(root)
        
        s = sentence.split(' ')
        res = []
        for w in s:
            res.append(tire.find_root(w))
        
        return ' '.join(res)


class Solution2:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        
        root = set(dict)
        
        def replace(word):
            for i in range(len(word)):
                if word[:i+1] in root:
                    return word[:i+1]
            return word
        
        res = []
        for word in sentence.split():
            res.append(replace(word))
        
        return ' '.join(res)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.replaceWords
            self.assertEqual(func(["cat","bat","rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")

if __name__ == '__main__':
    unittest.main()