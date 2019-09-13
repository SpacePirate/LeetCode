"""
53. Maximum Subarray (Easy, 43.5%)

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
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
    Runtime: 44 ms, faster than 90.96% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 13.7 MB, less than 40.03% of Python3 online submissions for Maximum Subarray.
    """
    # Complexity: O(n)
    # Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        
        max_sum = nums[0]
        cur_sum = nums[0]

        for n in nums[1:]:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)

        return max_sum

@my_timer
def test_case(nums: List[int]):
    ans = Solution().maxSubArray(nums)
    print("Input: {}\nOutput: {}".format(nums, ans))

if __name__ == "__main__":
    test_case([1])
    test_case([-2,1,-3,4,-1,2,1,-5,4])

