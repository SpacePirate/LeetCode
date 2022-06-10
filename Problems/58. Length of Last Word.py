"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

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

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.str = s.strip()
        self.len = len(self.str)
        self.beg = 0
        # Get the index of first white space from the end
        beg = self.len-2
        while (beg > 0 ):
            if self.str[beg] == " " and self.str[beg+1] != " ": 
                self.beg = beg + 1
                break
            beg -= 1 
 
        return self.len - self.beg

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().lengthOfLastWord(*args, **kwargs)
    return ans
    
if __name__ == "__main__":
    arg = "Hello World"
    ans = test_case(arg)
    print("The last word is {0} letters long.".format(ans))
    arg = "   fly me   to   the moon  "
    ans = test_case(arg)
    print("The last word is {0} letters long.".format(ans))
    arg = "luffy is still joyboy"
    ans = test_case(arg)
    print("The last word is {0} letters long.".format(ans))
    arg = "    day"
    ans = test_case(arg)
    print("The last word is {0} letters long.".format(ans))
