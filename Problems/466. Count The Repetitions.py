"""
Define S = [s,n] as the string S which consists of n connected strings s. 
For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 
if we can remove some characters from s2 such that it becomes s1. 
For example, “abc” can be obtained from “abdbec” based on our definition, 
but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and 
two integers 0 ≤ n1 ≤ 10^6 and 1 ≤ n2 ≤ 10^6. Now consider the strings S1 and S2, 
where S1=[s1,n1] and S2=[s2,n2]. 
Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
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
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        M = 0
        # Check if S2 can be obatined from S1
        for s in s2:
            # All characters in s2 should exist in s1
            if s not in s1: return M
        
        # Now there is at least one repetition, remove unused characters
        new_s1 = ""
        for s in s1:
            if s in s2: new_s1 += s

        S1 = new_s1 * n1
        S2 = s2 * n2
        print("S1: {}".format(new_s1))
        print("S2: {}".format(s2))

        n_s2 = 0
        for s in S1:
            if s == S2[n_s2]: n_s2 += 1
            if n_s2 == len(S2):
                M += 1
                n_s2 = 0

        return M

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().getMaxRepetitions(*args, **kwargs)
    print("Input: {0},{1}".format(*args, **kwargs))
    print("Output: {0}".format(ans))

if __name__ == "__main__":
    test_case("acb", 4, "ab", 2)
    test_case("baba", 11, "baab", 1)
    test_case("nlhqgllunmelayl", 10000, "lnl", 10)
    S1 = "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf"
    S2 = "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly"
    test_case(S1, 100000, S2, 1)