"""
914. X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that 
it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
 
Constraints:
1 <= deck.length <= 10^4
0 <= deck[i] < 10^4

"""

from typing import List
from fractions import gcd

def my_timer(func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        s = int(t2)
        ms = int(t2*10**3)
        us = int(t2*10**6)
        dt = "{}.{}.{}s".format(s, ms, us)
        print('{0} ran in : {1}'.format(func.__name__, dt))
        return result
    return wrapper

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        N = len(deck)
        if N == 1: return False
        
        # Count the cards
        groups = {}
        for card in deck:
            if card in groups: groups[card] += 1
            else: groups[card] = 1

        # For every possible group size X check if all groups are equally separable
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in groups.values()): return True

        return False
        
@my_timer
def test_case(*args, **kwargs):
    ans = Solution().hasGroupsSizeX(*args, **kwargs)
    print("Answer is {0}".format(ans))
    return ans
    
if __name__ == "__main__":
    arg = [1,2,3,4,4,3,2,1]
    ans = test_case(arg)
    arg = [1,1,1,2,2,2,3,3]
    ans = test_case(arg)
    arg = [1]
    ans = test_case(arg)
    arg = [1,1,2,2,2,2]
    ans = test_case(arg)
    arg = [1,1,1,2,2,2,3,3]
    ans = test_case(arg)
