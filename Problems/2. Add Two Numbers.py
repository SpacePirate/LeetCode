"""
2. Add Two Numbers (Medium, 31.1%)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def readDigits(self, l: ListNode) -> int:
        while l != None: 
            yield l.val
            l = l.next
            
    def listNodeToDigits(self, l: ListNode) -> int:
        val = 0
        for idx, num in enumerate(self.readDigits(l)): val += num * (10**idx)
        return val

    def printListNode(self, l: ListNode):
        ans = []
        for num in self.readDigits(l): ans.append(num)
        print(ans)

    def digitsToListNode(self, num: int) -> ListNode:
        if num >= 10:
            d = num % 10
            num = num//10
            l = ListNode(d)
            l.next = self.digitsToListNode(num)
            return l
        else:
            l = ListNode(num)
            return l

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1 - ListNode with length n
        # l2 - ListNode with length m

        val1 = self.listNodeToDigits(l1) # Complexity: O(n), Space: O(1)
        val2 = self.listNodeToDigits(l2) # Complexity: O(m), Space: O(1)
        ans = val1 + val2
        
        # Complexity: O(max(n, m)), Space: O(max(n, m) + 1)
        return self.digitsToListNode(ans) 

def test_case(x, y):
    a = Solution().digitsToListNode(x)
    b = Solution().digitsToListNode(y)

    c = Solution().addTwoNumbers(a, b)

    ans = Solution().listNodeToDigits(c)
    print(ans)

    assert ans == (x + y)

if __name__ == "__main__":
    # test_case(345, 12)
    # test_case(0, 12)
    # test_case(12345678, 55)
    # test_case(999, 999)
    # test_case(0, 999)

    a_int1 = 100000000000000001
    a_int2 = 1000000000000000001
    b_int = 465

    test_case(a_int1, b_int)
    test_case(a_int2, b_int)

"""
Runtime: 84 ms, faster than 76.21% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.3 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
"""