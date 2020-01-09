'''
08/01/2020

126. Word Ladder II - Hard

Tag: Graph, BFS

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from typing import List
import collections

class Solution0:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        BFS:
        
        Algorithm:
        1. Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

        2. Push the key-value pair with beginWord as key and all the transformation sequence to this key word from beginWord into a dict Layers. for the beginWord, it's beginWord:[[beginWord]]. We return all the transformation sequence of the endWord at the end.

        3. To prevent cycles, use a visited dictionary.

        4. While the dict: Layers has elements, iterate the key, Let's call this word as current_word.
        
        5. If the current_word match with the endWord, append all the transformation sequence into result.
        
        6. Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

        7. The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

        8. Hence, for each word in this list of intermediate words, if it's not visted, append it to all the transformation sequence of the current_word, to form a list of tranformation sequence to the word which the current_word can transformate to. next_layer[word] += [path + [word] for path in layer[curr_word]]

        9. For all the word in the next_layer, mark them visted.
        
        10. Replace the Layer with next layer and do the above again.
        
        11. Return the result.
        
        

        Time: O(M×N), where M is the length of words and N is the total number of words in the input word list.
        Space: O(M×N), to store all M transformations for each of the N words, in the all_combo_dict dictionary. Visited dictionary is of N + MXN size
        
        '''
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        
        # all the words have the same length
        self.length = len(beginWord)
        
        # Dict to hold combination of words that can be formed,
        # from any given word, by changing one letter at a time.
        self.all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(self.length):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        # layer store all possible transformation to the current key word
        layer = {beginWord:[[beginWord]]}
        # Visited to make sure we don't repeate processing same word
        visited = {beginWord:True}
        # list to store result
        res = []
        
        while layer:
            next_layer = collections.defaultdict(list)
            for curr_word in layer:
                # if match the endword, append the transformation into result
                if curr_word == endWord:
                    res += layer[curr_word]
                    
                for i in range(self.length):
                    itermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                    for word in self.all_combo_dict[itermediate_word]:
                        if word not in visited:
                            next_layer[word] += [seq + [word] for seq in layer[curr_word]]
            # add the key of this layer into visited, avoid duplicate
            for key in next_layer:
                visited[key] = True
            # update the layer to next layer
            layer = next_layer

        return res


class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        Bidirectional BFS:
        
        Algorithm:
        1. The algorithm is very similar to the standard BFS based approach we saw earlier.

        2. The only difference is we now do BFS starting two nodes instead of one. This also changes the termination condition of our search.

        3. We now have two visited dictionaries to keep track of nodes visited from the search starting at the respective ends.

        4. If we ever find a node/word which is in the visited dictionary of the parallel search we terminate our search, since we have found the meet point of this bidirectional search. It's more like meeting in the middle instead of going all the way through.
        
        5. The shortest transformation sequence is the sum of levels of the meet point node from both the ends. 
        
        Time: O(M×N), where M is the length of words and N is the total number of words in the input word list.Similar to one directional, bidirectional also takes M*N for finding out all the transformations. But the search time reduces to half, since the two parallel searches meet somewhere in the middle.
        Space: O(M×N), to store all M transformations for each of the N words, in the all_combo_dict dictionary, same as one directional. But bidirectional reduces the search space. It narrows down because of meeting in the middle.
        
        '''
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        
        # all the words have the same length
        self.length = len(beginWord)
        
        # Dict to hold combination of words that can be formed,
        # from any given word, by changing one letter at a time.
        self.all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(self.length):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        # layer store all possible transformation to the current key word
        layer_begin = {beginWord:[[beginWord]]}
        layer_end = {endWord:[[endWord]]}
        # Visited to make sure we don't repeate processing same word
        visited_begin = {beginWord:True}
        visited_end = {endWord:True}

        while layer_begin and layer_end:
            layer_begin, ans = self.visitWordNode(layer_begin, visited_begin, layer_end, visited_end)
            if ans:
                return ans
            layer_end, ans = self.visitWordNode(layer_end, visited_end, layer_begin, visited_begin, flip=True)
            if ans:
                return ans
        
        return ans
            
    def visitWordNode(self, layer, visited, other_layer, other_visited, flip=False):
        next_layer = collections.defaultdict(list)
        res = []
        for curr_word in layer:
            for i in range(self.length):
                itermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                for word in self.all_combo_dict[itermediate_word]:
                    # if match the endword, append the transformation into result
                    if word in other_visited:
                        layer1 = layer[curr_word]
                        layer2= other_layer[word]
                        if flip:
                            # always put the layer_end later
                            layer1, layer2 = layer2, layer1
                        # for layer 2, reverse the order of result
                        res += [seq1+seq2[::-1] for seq1 in layer1 for seq2 in layer2]
                    if word not in visited:
                        next_layer[word] += [seq + [word] for seq in layer[curr_word]]
        # add the key of this layer into visited, avoid duplicate
        for key in next_layer:
            visited[key] = True
        # update the layer to next layer
        layer = next_layer
        return layer, res

# Unit Test
import unittest
class findLaddersCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findLaddersCase(self):

        func = Solution0().findLadders
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]])
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log"]), [])

        func = Solution1().findLadders
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]])
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log"]), [])

if __name__ == '__main__':
    unittest.main()