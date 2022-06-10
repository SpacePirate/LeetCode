"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
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

class Solution(object):
    def perm(self, nums, start, result):
        n = len(nums)
        if start == n-1:
            result.append(nums) 
            return 
        for j in range(start, n):
            nums[j], nums[start] = nums[start], nums[j] #swapping the elements
            # nums[:] = nums.copy() i.e, just makes the duplicate of the current array
            self.perm(nums[:], start+1, result)  
 
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans=[]
        self.perm(nums,0, ans)

        return ans

"""
Runtime: 28 ms, faster than 66.23% of Python online submissions for Permutations.
Memory Usage: 12.7 MB, less than 6.00% of Python online submissions for Permutations.
"""

@my_timer
def test_case(*args, **kwargs):
    ans = Solution().permute(*args, **kwargs)
    print("Input: {0}".format(*args))
    print("Output: {0}".format(ans))

if __name__ == "__main__":
    test_case([1,2,3])
