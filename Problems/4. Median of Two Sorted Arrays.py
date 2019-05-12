"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from typing import List

class Solution:
    def getMedian(self, nums: List[int]) -> float:
        """ Find the median value of a non-empty list of integers."""
        n = len(nums)
        m = n//2
        assert(n > 0)
        # Odd list
        if n % 2: return float(nums[m])
        # Even list
        else:     return (nums[m-1] + nums[m])/2.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Put shorter list first
        listA, listB = sorted((nums1, nums2), key=len)

        n = len(listA)
        m = len(listB)
        assert m >= n
        assert not (n == 0 and m == 0) # both can't be empty lists
        assert m != 0 # larger list can't be empty (same as above)

        len_max = n + m
        mid_max = len_max//2

        i_min = 0
        i_max = n
        # Perform binary search. O(log(n+m))
        while i_min <= i_max:
            i = (i_min+i_max)//2
            j = mid_max - i
            # Since listB is always longer than listA, len_max-i is never negative
            left  = listA[:i] + listB[:j]
            right = listA[i:] + listB[j:] 
            print("i = {0}, j = {1}, left = {2}, right = {3}".format(i, j, left, right))

            # largest listB in left group is greater than the smallest list A in right group
            if   i < n and listB[j-1] > listA[i]: i_min = i + 1 # i needs to increase
            # largest listA in left group is greater than the smallest list B in right group
            elif i > 0 and listA[i-1] > listB[j]: i_max = i - 1 # i needs to decrease
            # found i for median
            else:
                print("Median indicies: i = {0}, j = {1}".format(i, j))
                if i == n: min_right = listB[j]
                elif j == m: min_right = listA[i]
                else: min_right = min(listA[i], listB[j])

                # Odd List
                if len_max % 2: return float(min_right)
                # Even List
                else: 
                    if i == 0: max_left = listB[j-1]
                    elif j == 0: max_left = listA[i-1]
                    else: max_left = max(listA[i-1], listB[j-1])

                    return (max_left + min_right)/2.0

        # Not found
        return -1
        
def test_case(nums1: List[int], nums2: List[int]):
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("Meadian is {0}".format(ans))

if __name__ == "__main__":
    test_case([2], [1,3])
    test_case([1,2], [3,4])
    # test_case([-1,2], [-3,4])
    # test_case([1,2,3], [])
    # test_case([], [4,5,6])

"""
Runtime: 
84 ms, faster than 59.00% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 
13.2 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.
"""