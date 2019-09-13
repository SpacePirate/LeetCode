"""
29. Divide Two Integers (Medium)
Given two integers dividend and divisor, divide two integers without using multiplication, 
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
-Both dividend and divisor will be 32-bit signed integers.
-The divisor will never be 0.
-Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
For the purpose of this problem, assume that your function returns 2**31 − 1 when 
the division result overflows.
"""

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
    # TOO SLOW
    def divide_brute(self, dividend: int, divisor: int) -> int:
        assert (divisor != 0)
        assert (dividend <= (2**31)-1 and dividend >= -(2**31))
        assert ( divisor <= (2**31)-1 and  divisor >= -(2**31))

        sign = 1
        if dividend < 0: sign = sign * -1
        if  divisor < 0: sign = sign * -1
        remain = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1: 
            quotient = sign * remain
            if quotient >= (2**31): quotient = (2**31)-1
            return quotient
        result = 0
        while (remain >= divisor):
            remain -= divisor
            result += 1
        return sign*result

    """
    Runtime: 32 ms, faster than 99.56% of Python3 online submissions for Divide Two Integers.
    Memory Usage: 13.3 MB, less than 17.52% of Python3 online submissions for Divide Two Integers.
    """
    # Time: O(log_m(n)), where n = dividend and m = divisor
    # Spoce: O(1)
    def divide(self, dividend: int, divisor: int) -> int:
        assert (divisor != 0)
        assert (dividend <= (2**31)-1 and dividend >= -(2**31))
        assert ( divisor <= (2**31)-1 and  divisor >= -(2**31))

        sign = 1
        if dividend < 0: sign = sign * -1
        if  divisor < 0: sign = sign * -1
        remain = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1: 
            quotient = sign * remain
            if quotient >= (2**31): quotient = (2**31)-1
            return quotient
        result = 0
        temp_divisor = divisor
        # Outer loop handles one subtraction at a time. O(n)
        while (remain >= divisor):
            # Double subtraction amount until it overshoots
            temp_divisor = divisor
            temp_result = 1
            while (remain >= temp_divisor):
                remain -= temp_divisor
                result += temp_result # Accumulate
                temp_divisor += temp_divisor # Double subtraction amount
                temp_result  += temp_result

        return sign*result

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().divide(*args, **kwargs)
    print("Input: {0},{1}".format(*args, **kwargs))
    print("Output: {0}".format(ans))

if __name__ == "__main__":
    test_case(10, 3)
    test_case(7, -3)
    test_case(8, -2)
    test_case(-1, 1)
    test_case(-1, -1)
    test_case(1, -1)
    test_case(15, -1)