"""
16/09/2019
621. Task Scheduler - Medium
Tag: Other, Heap

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""

from typing import List
from heapq import heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        https://leetcode.com/problems/task-scheduler/discuss/184769/Compiled-3-Approaches-python-solution-with-complexity-analysis-perfect-for-interviews
        """
        # init the time and heap
        time, hq = 0, []
        schedule = []
        cnt = Counter(tasks)
        for task, freq in cnt.items():
            heappush(hq, (-freq, task))
        
        print(f"hq: {hq}")
        while hq:
            t, temp = 0, []
            while t <= n:
                time += 1
                print(f"time: {time}, hq: {hq}")
                print(f"t: {t}, temp: {temp}")
                if hq:
                    freq, task = heappop(hq)
                    schedule.append(task)
                    if freq < -1: # freq is negative. if freq >= -1, means it has completed
                        # freq minus 1 and push it back
                        heappush(temp, (freq+1, task))
                if not hq and not temp:
                    break
                t += 1
            for item in temp:
                heappush(hq, item)
        
        print(f"res: {schedule}, time: {time}")
        return time

# Unit Test
import unittest
class leastIntervalCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_leastInterval(self):
        func = Solution().leastInterval
 

        self.assertEqual(func(["A","A","A","B","B","B"], 2), 8)
        self.assertEqual(func(["A","A","A","B","B","B", "C", "D"], 2), 8)









if __name__ == '__main__':
    unittest.main()


