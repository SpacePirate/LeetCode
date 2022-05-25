"""
000. Title

Problem description
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

class Solution:
    def template(self, arg: List[int]) -> int:
        return 0

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().template(*args, **kwargs)
    return ans
    
if __name__ == "__main__":
    arg = [3,0]
    ans = test_case(arg)
