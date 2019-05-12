"""
2. Add Two Numbers

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
        while True:
            yield l.val if l != None else 0
            try: l = l.next
            except AttributeError: l = ListNode(0)

    def digitsToListNode(self, num: int) -> ListNode:
        l_out = None
        l_prev = None
        while num > 0:
            d = num % 10
            num = num/10
            if l_prev == None:
                l_out = ListNode(d)
                l_prev = l_out
            else:
                l_prev.next = ListNode(d)

        return l_out
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        for idx, (val1, val2) in enumerate(zip(self.readDigits(l1), self.readDigits(l2))):
            if (val1 + val2 == 0): break
            sum += (val1 + val2) * (10^idx)
        
        return self.digitsToListNode(sum)

