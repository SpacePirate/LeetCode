"""
1672. Richest Customer Wealth (Easy)
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money 
the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

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

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 56 ms, faster than 49.16% of Python3 online submissions for Richest Customer Wealth.
        Memory Usage: 14.2 MB, less than 82.90% of Python3 online submissions for Richest Customer Wealth.
        """
        # Time: O(n^2)
        # Spoce: O(1)
        return max([sum(x) for x in accounts])


    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 48 ms, faster than 92.36% of Python3 online submissions for Richest Customer Wealth.
        Memory Usage: 14.3 MB, less than 26.24% of Python3 online submissions for Richest Customer Wealth.
        """
        # Time: O(n^2)
        # Spoce: O(1)
        richest = -9e99999
        for a in accounts:
            wealth = sum(a)
            if wealth > richest: richest = wealth

        return richest

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().maximumWealth(*args, **kwargs)
    print(ans)
    # print("Input: {0},{1}".format(*args, **kwargs))
    # print("Output: {0}".format(ans))

if __name__ == "__main__":
    customers = [
        [0],
        [0, 0],
        [1, 2, 3],
        [4, 5],
        [4, 4], 
        [-1, 0]
        ]
    test_case(customers)