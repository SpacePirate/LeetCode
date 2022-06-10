"""
66. Plus One

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

"""

from typing import List
from unicodedata import digit

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
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        carry = 0
        for i in range(n):
            d = digits[n-i-1] + carry
            if i == 0: d += 1
            if d == 10:
                carry = 1
                d = 0
            else: carry = 0
            digits[n-i-1] = d
            
        if carry == 1: digits = [1] + digits

        return digits

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().plusOne(*args, **kwargs)
    print(ans)
    return ans
    
if __name__ == "__main__":
    arg = [1, 2, 3]
    ans = test_case(arg)
    arg = [9]
    ans = test_case(arg)
    arg = [4, 3, 2, 1]
    ans = test_case(arg)
