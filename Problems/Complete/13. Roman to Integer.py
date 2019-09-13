"""
13. Roman to Integer (Easy, 52.3%)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

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
    """
    Runtime: 76 ms, faster than 66.71% of Python3 online submissions for Roman to Integer.
    Memory Usage: 13.3 MB, less than 54.29% of Python3 online submissions for Roman to Integer.
    """
    # Complexity: O(n)
    # Space: O(n)
    def romanToInt(self, s: str) -> int:
        n = len(s)
        c = n-1
        num = 0
        while (c >= 0):
            if s[c] == "I":   num += 1 if num < 5 else -1
            elif s[c] == "V": num += 5
            elif s[c] == "X": num += 10 if num < 50 else -10
            elif s[c] == "L": num += 50
            elif s[c] == "C": num += 100 if num < 500 else -100
            elif s[c] == "D": num += 500
            elif s[c] == "M": num += 1000
            # Invalid character
            else: assert ValueError
            c -= 1

        return num 

    """
    Runtime: 52 ms, faster than 99.48% of Python3 online submissions for Roman to Integer.
    Memory Usage: 13.3 MB, less than 62.60% of Python3 online submissions for Roman to Integer.
    """
    # Complexity: O(1)
    # Space: O(n)
    def romanToInt2(self, s: str) -> int:
        rom_dict = { "I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000
        }
        # Replace all subtract cases
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        num = 0
        for char in s: num += rom_dict[char]

        return num

@my_timer
def test_case(s: str):
    ans = Solution().romanToInt(s)
    print("Input: {}\nOutput: {}".format(s, ans))

if __name__ == "__main__":
    test_case("VI")
    test_case("IV")

