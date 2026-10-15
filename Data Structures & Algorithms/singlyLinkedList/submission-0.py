class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node
        if self.tail is None:      # list was empty
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail is None:      # list was empty
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:  # removed the only node
                self.tail = None
            return True

        # walk to the node just before the one we're removing
        prev = self.head
        i = 0
        while prev and i < index - 1:
            prev = prev.next
            i += 1

        if prev is None or prev.next is None:
            return False

        target = prev.next
        prev.next = target.next
        if target is self.tail:    # removed the last node
            self.tail = prev
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res