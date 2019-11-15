"""
15/11/2019
1117. Building H2O - Medium
Tag: Concurrency, Mutex, Semaphore

There are two kinds of threads, oxygen and hydrogen. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
We don’t have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

Example 1:

Input: "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
 

Constraints:

Total length of input string will be 3n, where 1 ≤ n ≤ 20.
Total number of H will be 2n in the input string.
Total number of O will be n in the input string.

"""

from threading import Lock
from threading import Semaphore

class H2O:
    def __init__(self):
        self.out = Lock()
        self.h = Semaphore(2)
        self.o = Semaphore(2)
        # acquire the h and o
        self.h.acquire()
        self.h.acquire()
        self.o.acquire()
        self.o.acquire()
        

    
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        self.h.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.o.release()





    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # acquire lock
        self.out.acquire()
        # release h lock, so two Hydrogen can be release
        self.h.release()
        self.h.release()
        # two Hydrogen avaiable now, release one Oxxygen.
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # acquire o lock, what for next two Hydrogen
        self.o.acquire()
        self.o.acquire()
        # release lock
        self.out.release()

