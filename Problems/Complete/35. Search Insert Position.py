"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4

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
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        beg, end = 0, len(nums)-1

        while beg <= end:
            mid = int((beg+end)/2)
            if nums[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        
        return beg

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().searchInsert(*args, **kwargs)
    print("Answer is {0}".format(ans))
    return ans
    
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    ans = test_case(nums, target)
    
    nums = [1,3,5,6]
    target = 2
    ans = test_case(nums, target)

    nums = [1,3,5,6]
    target = 7
    ans = test_case(nums, target)
