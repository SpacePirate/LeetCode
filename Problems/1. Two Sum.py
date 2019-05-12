"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific 
target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List

class Solution:
    # Time: O(n^2), Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            diff = target - val
            future_nums = nums[idx+1:]
            if diff in future_nums:
                pair_idx = future_nums.index(diff) + idx + 1
                return [idx, pair_idx]

def test_case(x: List[int], y: int):
    ans = Solution().twoSum(x, y)
    print(ans)

if __name__ == "__main__":
    test_case([3,2,4], 6)

"""
Runtime: 840 ms, faster than 35.07% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 36.61% of Python3 online submissions for Two Sum.
"""