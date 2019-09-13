"""
468. Validate IP Address (Medium)

Write a function to check whether an input string is a valid IPv4 address or 
IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, 
which consists of four decimal numbers, each ranging from 0 to 255, 
separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits,
each group representing 16 bits. The groups are separated by colons (":").
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. 
Also, we could omit some leading zeros among four hexadecimal digits and 
some low-case characters in the address to upper-case ones, 
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group 
using two consecutive colons (::) to pursue simplicity. 
For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. 
For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

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
    """
    Runtime: 32 ms, faster than 99.39% of Python3 online submissions for Validate IP Address.
    Memory Usage: 13.2 MB, less than 51.49% of Python3 online submissions for Validate IP Address.
    """
    # Time: O(n)
    # Space: O(1)
    def validIPAddress(self, IP: str) -> str:
        # Check for IPv4
        if "." in IP:
            addr = IP.split(".")
            if len(addr) != 4: return "Neither"
            for num in addr:
                if len(num) > 3: return "Neither"
                try: n = int(num)
                except: return "Neither"
                if str(n) != num: return "Neither" # Leading zeros are invalid
                if n < 0 or n > 255: return "Neither"
            return "IPv4"
        # Check for IPv6
        if ":" in IP:
            addr = IP.split(":")
            if len(addr) != 8: return "Neither"
            for num in addr:
                if len(num) > 4: return "Neither"
                try: n = int(num, 16)
                except: return "Neither"
                if num[0] == "-": return "Neither" # Leading zeros are allowed
                if n < 0 or n > 65535: return "Neither"
            return "IPv6"
        return "Neither"

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().validIPAddress(*args, **kwargs)
    print("Input: {}\nOutput: {}".format(*args, ans))

if __name__ == "__main__":
    test_case("172.16.254.1")
    test_case("2001:0db8:85a3:0:0:8A2E:0370:7334")
    test_case("2001:0db8:85a3:0:0:8A2E:0370:7334:")
    test_case("2001:0db8:85a3:00000:0:8A2E:0370:7334")
    test_case("20EE:FGb8:85a3:0:0:8A2E:0370:7334")
    test_case("1081:db8:85a3:01:-0:8A2E:0370:7334")