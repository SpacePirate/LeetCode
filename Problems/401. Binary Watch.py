"""
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), 
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are currently on, 
return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, 
for example "10:2" is not valid, it should be "10:02".
"""
from typing import List
import math

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
    # Brute force method
    # Time: O(h * m * n)
    def readBinaryWatch1(self, num: int) -> List[str]:
        times =[]
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    times.append('%d:%02d' % (h, m))

        return times

    def readBinaryWatch(self, num: int) -> List[str]:
        assert (num > 0 and num <= 10) # What does n = 0 mean?
        max_num = 2**10 - 1
        ones = 2**num - 1 # Get trailing ones
        high = int(round(math.log(num, 2))) # Get index of highest one bit position

        # All LEDs are on
        if ones == max_num:
            
        while (ones < max_num and high > 0):
            

            high -= 1
            

        return num


@my_timer
def test_case(*args, **kwargs):
    ans = Solution().readBinaryWatch(*args, **kwargs)
    print("Input: {0},{1}".format(*args, **kwargs))
    print("Output: {0}".format(ans))
