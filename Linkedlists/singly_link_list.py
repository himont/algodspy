class Node:

    def __init__(self, value):
        """
        Initialize your data structure here.
        """
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self, value=None):
        """
        Initialize your data structure here.
        """
        if value:
            self.head = Node(value)
        else:
            self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        count = 0
        cur = self.head
        if not cur:
            return -1
        while True:
            if count == index:
                return cur.val
            elif count < index:
                if cur.next:
                    cur = cur.next
                    count += 1
                else:
                    return -1
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        cur = Node(val)
        if self.head:
            cur.next = self.head
        self.head = cur

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        count = 0
        cur = self.head
        while count < index:
            if not cur:
                return
            prev = cur
            cur = cur.next
            count += 1
        prev.next = Node(val)
        prev.next.next = cur

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        cur = self.head
        while count < index:
            if not cur:
                return
            prev = cur
            cur = cur.next
            count += 1
        if cur:
            prev.next = cur.next
        else:
            prev.next = None


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(4)
    obj.addAtTail(9)
    obj.addAtIndex(1, 23)
    print(obj.get(1))
    obj.deleteAtIndex(2)
