'''
08/01/2020

127. Word Ladder - Medium

Tag: Graph, BFS

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from typing import List
import collections

class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        BFS:
        
        Algorithm:
        1. Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

        2. Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node. We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

        3. To prevent cycles, use a visited dictionary.

        4. While the queue has elements, get the front element of the queue. Let's call this word as current_word.

        5. Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

        6. The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

        7. Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

        8. Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.
        

        Time: O(M×N), where M is the length of words and N is the total number of words in the input word list.
        Space: O(M×N), to store all M transformations for each of the N words, in the all_combo_dict dictionary. Visited dictionary is of N + MXN size
        
        '''
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        # all the words have the same length
        L = len(beginWord)
        
        # Dict to hold combination of words that can be formed,
        # from any given word, by chaning one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeate processing same word
        visited = {beginWord:True}
        while queue:
            curr_word, level = queue.popleft()
            for i in range(L):
                itermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                if itermediate_word in visited:
                    continue
                # get all the words which share the same itermediate word
                for word in all_combo_dict[itermediate_word]:
                    # if match the endword, return the answer
                    if word == endWord:
                        return level+1
                    # if word not visited, add it to the queue and mark as visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                visited[itermediate_word] = True
        
        return 0




class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Bidirectional BFS:
        
        Algorithm:
        1. The algorithm is very similar to the standard BFS based approach we saw earlier.

        2. The only difference is we now do BFS starting two nodes instead of one. This also changes the termination condition of our search.

        3. We now have two visited dictionaries to keep track of nodes visited from the search starting at the respective ends.

        4. If we ever find a node/word which is in the visited dictionary of the parallel search we terminate our search, since we have found the meet point of this bidirectional search. It's more like meeting in the middle instead of going all the way through.
        
        5. The shortest transformation sequence is the sum of levels of the meet point node from both the ends. Thus, for every visited node we save its level as value in the visited dictionary.
        
        Time: O(M×N), where M is the length of words and N is the total number of words in the input word list.Similar to one directional, bidirectional also takes M*N for finding out all the transformations. But the search time reduces to half, since the two parallel searches meet somewhere in the middle.
        Space: O(M×N), to store all M transformations for each of the N words, in the all_combo_dict dictionary, same as one directional. But bidirectional reduces the search space. It narrows down because of meeting in the middle.
        
        '''
        
          
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        # all the words have the same length
        self.length = len(beginWord)
        
        # Dict to hold combination of words that can be formed,
        # from any given word, by chaning one letter at a time.
        self.all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(self.length):
                # key is the generic word
                # value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)
        
        # Queue for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)])
        queue_end = collections.deque([(endWord, 1)])
        ans = None

        # Visited to make sure we don't repeate processing same word
        visited_begin = {beginWord:1}
        visited_end = {endWord:1}
        
        
        while queue_begin and queue_end:
            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        
        return 0
    
    def visitWordNode(self, queue, visited, other_visited):
        
            curr_word, level = queue.popleft()
            for i in range(self.length):
                itermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                if itermediate_word in visited:
                    continue
                # get all the words which share the same itermediate word
                for word in self.all_combo_dict[itermediate_word]:
                    # if the word has already been visited from the other parallel traversal, this means we have found the answer.
                    if word in other_visited:
                        return level+other_visited[word]
                    # if word not visited, add it to the queue and mark as visited
                    if word not in visited:
                        visited[word] = level+1
                        queue.append((word, level+1))
                visited[itermediate_word] = True
        
            return None

# Unit Test
import unittest
class ladderLengthCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ladderLengthCase(self):
        func = Solution1().ladderLength
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log"]), 0)

        func = Solution2().ladderLength
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(func("hit", "cog", ["hot","dot","dog","lot","log"]), 0)

if __name__ == '__main__':
    unittest.main()