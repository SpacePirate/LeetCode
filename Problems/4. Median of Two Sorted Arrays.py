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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
               
        len1 = len(nums1)
        len2 = len(nums2)
        len_max = len1 + len2
        assert not (len1 == 0 and len2 == 0)        
        mid_max = len_max//2
        

        for 
        
        # # Even list
        # if len_max % 2 == 0:
        #     return (eval_list[mid_len-1] + eval_list[mid_len])/2.0
        # # Odd list
        # else:
        #     return float(eval_list[mid_len])

def test_case(nums1: List[int], nums2: List[int]):
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print(ans)

if __name__ == "__main__":
    test_case([1,3], [2])
    test_case([1,2], [3,4])
    test_case([-1,2], [-3,4])
    test_case([1,2,3], [])
    test_case([], [4,5,6])