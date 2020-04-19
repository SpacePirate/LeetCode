"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
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

class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # First toss negative numbers
        if x < 0: return False

        x = str(x)
        n = len(x)

        ans = True
        for i in range(int(n/2)):
            if x[i] != x[n-i-1]:
                ans = False
                break 
            
        return ans
        
        """
        Runtime: 52 ms, faster than 63.66% of Python online submissions for Palindrome Number.
        Memory Usage: 12.6 MB, less than 6.03% of Python online submissions for Palindrome Number.
        """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # First toss negative numbers
        if x < 0: return False
        # Single digitss are always a palindrome
        if x < 10: return True
        # If lowest digit is a 0, number will never be a plindrome
        if x % 10 == 0: return False

        # Reverse the lower half of the number and compare to upper half
        x_lower = 0;
        x_upper = x
        while(x_upper > x_lower):
            x_lower = x_lower * 10 + x_upper % 10
            x_upper = int(x_upper/10)

        # Ignore middle digit for odd number length integers
        ans = x_upper == x_lower or x_upper == int(x_lower/10)
        return ans

        """
        Runtime: 48 ms, faster than 76.32% of Python online submissions for Palindrome Number.
        Memory Usage: 12.7 MB, less than 6.03% of Python online submissions for Palindrome Number.
        """
        
@my_timer
def test_case(*args, **kwargs):
    ans = Solution().isPalindrome(*args, **kwargs)
    print("Input: {0}".format(*args))
    print("Output: {0}".format(ans))

if __name__ == "__main__":
    test_case(121)
    test_case(-121)
    test_case(0)
    test_case(10)
    test_case(100)
    test_case(21120)
    test_case(123321)
    test_case(321123)
