"""
707. Design Linked List

Design your implementation of the linked list. 
You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute prev to indicate the 
previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. 
             If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. 
                 After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. 
                         If index equals to the length of linked list, 
                         the node will be appended to the end of linked list. 
                         If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
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

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.size > 0 and index < self.size:
            node = self.getNodeAtIndex(index)
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.head.next = self.tail
            self.tail = new_node
            self.tail.prev = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.size == 0:
            self.tail = new_node
            self.tail.prev = self.head
            self.head = new_node
            self.head.next = self.tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def getNodeAtIndex(self, index: int) -> Node:
        # Allow negative indexingS
        if index < 0: index = self.size - (abs(index) % self.size) - 1
        # Search from tail
        if self.size - index >= self.size//2:
            count = self.size-1
            node = self.tail
            while count > index:
                node = node.prev
                count -= 1
        # Search from head
        else:
            count = 0
            node = self.head
            while count < index:
                node = node.next
                count += 1
                
        return node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the 
        end of linked list. If index is greater than the length, the node will not be inserted.
        """    
        # Ignore invalid index
        if index <= self.size and index >= 0:
            if index == 0: self.addAtHead(val)
            elif index == self.size: self.addAtTail(val)
            else:
                node = self.getNodeAtIndex(index)
                new_node = Node(val)
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # Ignore invalid index
        if index < self.size and index >= 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            # Remove head
            elif index == 0: 
                self.head = self.head.next
                self.head.prev = None
            # Remove tail
            elif index == self.size-1: 
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node = self.getNodeAtIndex(index)
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
            self.size -= 1

    def __repr__(self):
        if self.size == 0:
            return str([])
        elif self.size == 1:
            return str([self.head.val])
        else:
            my_listA = []
            my_node = self.head
            while True:
                my_listA.append(my_node.val)
                my_node = my_node.next
                if my_node == None: break

            my_listB = []
            my_node = self.tail
            while True:
                my_listB.append(my_node.val)
                my_node = my_node.prev
                if my_node == None: break
            my_listB.reverse()
            try: assert my_listA == my_listB
            except: return "Error: " + str(my_listA) + ", " + str(my_listB)
            return str(my_listA)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == "__main__":
    import random
    obj = MyLinkedList()
    obj.addAtHead(7)
    print(obj)
    obj.addAtHead(2)
    print(obj)
    obj.addAtHead(1)
    obj.addAtIndex(3,0)
    obj.deleteAtIndex(2)
    print(obj)
    obj.addAtHead(6)
    obj.addAtTail(4)
    print(obj)
    print(obj.get(4))
    print(obj)
    # for i in range(20): obj.addAtHead(random.randrange(1000))
    # print(obj)
    # for i in range(20): obj.addAtTail(random.randrange(1000))
    # print(obj)
    # for i in range(20): obj.deleteAtIndex(random.randrange(0, 100))
    # print(obj)
    # for i in range(20): obj.addAtIndex(random.randrange(50), random.randrange(1000))
    # print(obj)
    # for i in range(20): obj.addAtTail(random.randrange(1000))
    # print(obj)
    # for i in range(100): obj.get(random.randrange(-100, 100))
    # print(obj)