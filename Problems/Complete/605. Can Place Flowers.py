"""
605. Can Place Flowers (Easy)

Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots -
they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, 
where 0 means empty and 1 means not empty), and a number n, 
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""

import math
from typing import List

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

class Solution:
    """
    Runtime: 52 ms, faster than 93.74% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 13.2 MB, less than 78.69% of Python3 online submissions for Can Place Flowers.
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_bed = len(flowerbed)
        max_n = math.ceil(len_bed/2)
        assert (n >= 0 and n <= len_bed)

        possible = 0
        occupied = sum(flowerbed)
        prev = 0
        for i in range(len_bed):
            if flowerbed[i] == 0:
                if prev == 0:
                    flowerbed[i] = 1
                    prev = 1
                    possible += 1
                else: prev = 0
            else:
                if prev == 1:
                    flowerbed[i-1] == 0
                    possible -= 1
                else: prev = 1

        return n <= possible

@my_timer
def test_case(*args, **kwargs):
    print("Input: {0}, {1}".format(*args, **kwargs))
    ans = Solution().canPlaceFlowers(*args, **kwargs)
    print("Output: {0}".format(ans))

if __name__ == "__main__":
    test_case([1,0,0,0,0,1], 2)