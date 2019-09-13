"""
7. Reverse Integer (Easy, 25.3%)

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when 
the reversed integer overflows.

"""

def my_timer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.clock()
        result = func(*args, **kwargs)
        t2 = time.clock() - t1
        s = int(t2)
        ms = int(t2*10**3)
        us = int(t2*10**6)
        dt = "{}.{}.{}s".format(s, ms, us)
        print('{0} ran in : {1}'.format(func.__name__, dt))
        return result

    return wrapper

class Solution:
    def reverse_brute(self, x: int) -> int:
        """
        Runtime: 56 ms
        Memory Usage: 13.3 MB
        """
        valid_range = [-2**31, 2**31-1]
        num = list(str(abs(x)))
        num.reverse()
        num = int("".join(num))

        if num > valid_range[1] or num < valid_range[0]: num = 0

        if x < 0: return -1* num
        else:     return     num

    def modnum(self, x: int) -> int:
        while(x):
            yield x%10
            x = x//10 

    def reverse_generator(self, x: int) -> int:
        """
        Runtime: 40 ms, faster than 97.54% of Python3 online submissions for Reverse Integer.
        Memory Usage: 13.2 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
        """
        valid_range = [-2**31, 2**31-1]
        result = 0
        n = abs(x)
        for m in self.modnum(n): result = result*10 + m
        
        # Overflow
        if result > valid_range[1] or result < valid_range[0]: return 0
        # Return with correct sign
        if x < 0: return -1* result
        else:     return     result

    def reverse(self, x: int) -> int:
        """
        Runtime: 32 ms, faster than 99.71% of Python3 online submissions for Reverse Integer.
        Memory Usage: 13.2 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
        """
        valid_range = [-2**31, 2**31-1]
        result = 0
        n = abs(x)
        while n:
            result = result*10 + n%10
            n = n//10
        # Overflow
        if result > valid_range[1] or result < valid_range[0]: return 0
        # Return with correct sign
        if x < 0: return -1* result
        else:     return     result

@my_timer
def test_case(x: int):
    ans = Solution().reverse(x)
    print("Reversed {0} is {1}".format(x, ans))

if __name__ == "__main__":
    test_case(-123)
    test_case(12341235132)
    test_case(12341235)
    test_case(-123412341)
    test_case(12341324)

"""
Runtime: 32 ms, faster than 99.71% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.3 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
"""