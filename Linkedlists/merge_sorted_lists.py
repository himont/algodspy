import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        head = self.head
        while head is not None:
            print "%d ->" % head.value,
            head = head.next
        print "None"

    def addNodeEnd(self, node):
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = node

    def mergeSortedLists(self, list2):
        head1 = self.head
        head2 = list2.head
        final_head = None
        if head1.value > head2.value:
            final_head = head2
            head2 = head2.next
        else:
            final_head = head1
            head1 = head1.next
        prev = final_head
        while head2 is not None and head1 is not None:
            if head1.value > head2.value:
                prev.next = head2
                head2 = head2.next
            else:
                prev.next = head1
                head1 = head1.next
            prev = prev.next
        if head2 is None:
            prev.next = head1
        else:
            prev.next = head2
        return final_head

    def reverse(self):
        head1 = self.head
        prev = None
        next1 = head1.next
        # import ipdb; ipdb.set_trace()
        while next1 is not None:
            head1.next = prev
            prev = head1
            head1 = next1
            next1 = head1.next
        head1.next = prev
        return head1


if __name__ == "__main__":
    # arr1 = map(int, raw_input().strip().split(" "))
    arr1 = random.sample(range(1, 100), 10)
    arr2 = random.sample(range(1, 100), 10)
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    list1 = Linkedlist(Node(arr1[0]))
    list2 = Linkedlist(Node(arr2[0]))
    for i in range(1, len(arr1)):
        list1.addNodeEnd(Node(arr1[i]))
        list2.addNodeEnd(Node(arr2[i]))
    list1.printList()
    list2.printList()
    final_list = Linkedlist(list1.mergeSortedLists(list2))
    list1.printList
    final_list.printList()
    final_list.head = final_list.reverse()
    final_list.printList()
