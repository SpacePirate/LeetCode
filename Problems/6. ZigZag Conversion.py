"""
6. ZigZag Conversion (Medium, 31.3%)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

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
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1: return s # Just return the input

        result = ""
        # For numRows, zig-zag repeats every 2*(numRows-1) characters
        max_gap = 2*(numRows-1)
        for r in range(numRows):
            gap = 2*(numRows-r-1)
            idx = r
            print("Gap {}, idx {}".format(gap, idx))
            toggle = 1
            while(idx < n):
                result += s[idx]
                if (gap == 0) or (gap == max_gap): idx += max_gap
                else:
                    if toggle == 1:
                        idx += 2*(numRows-r-1)
                        toggle = -1
                    else:
                        idx += max_gap - 2*(numRows-r-1)
                        toggle = 1
        return result

@my_timer
def test_case(s: str, numRows: int):
    ans = Solution().convert(s, numRows)
    assert(len(ans) == len(s))
    print("Input: {}\nOutput: {}".format(s, ans))

if __name__ == "__main__":
    # test_case("123456789", 4)
    # test_case("A", 1)
    # test_case("AB", 1)
    # test_case("AB", 1)
    txt = """mpjevzguiuzzxoiblltwhbdogjogdofpeqvzqcwawvz"""
    test_case(txt, 3)

"""
Runtime: 64 ms, faster than 94.44% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.4 MB, less than 9.88% of Python3 online submissions for ZigZag Conversion.
"""