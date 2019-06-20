"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head == None:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head
            self.length = self.length + 1
            return

        self.head.insert_before(value)
        self.head = self.head.prev
        self.length = self.length + 1
        return

    def remove_from_head(self):
        if self.head == None:
            return None

        if self.head.next == None:
            value = self.head.value
            self.head.delete()
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return value

        value = self.head.value
        new_head = self.head.next
        self.head.delete()
        self.head = new_head
        self.length = self.length - 1
        return value

    def add_to_tail(self, value):
        if self.head == None:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head
            self.length = self.length + 1
            return

        self.tail.insert_after(value)
        self.tail = self.tail.next
        self.length = self.length + 1
        return

    def remove_from_tail(self):
        if self.head == None:
            return None

        if self.length == 1:
            value = self.tail.value
            self.tail.delete()
            self.head.delete()
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return value

        if self.length == 2:
            value = self.tail.value
            self.tail.delete()
            self.tail = self.head
            self.length = self.length - 1
            return value

        value = self.tail.value
        new_tail = self.tail.prev
        self.tail.delete()
        self.tail = new_tail
        self.length = self.length - 1
        return value

    def move_to_front(self, node):
        if self.length == 1:
            return

        if node.prev == None:
            return

        if node.next == None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.head.insert_before(node.value)
            self.head = self.head.prev
            return

        self.add_to_head(node.value)
        node.delete()
        self.length = self.length - 1
        return

    def move_to_end(self, node):
        if self.length == 1:
            return

        if node.next == None:
            return

        if node.prev == None:
            self.head = self.head.next
            self.head.prev = None
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
            return

        self.add_to_tail(node.value)
        node.delete()
        self.length = self.length - 1
        return

    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return

        if node.prev == None:
            self.head = self.head.next
            self.head.prev.delete()
            self.length = self.length - 1
            return

        if node.next == None:
            self.tail = self.tail.prev
            self.tail.next.delete()
            self.length = self.length - 1
            return

        node.delete()
        self.length = self.length - 1
        return

    def get_max(self):
        max = self.head.value
        node = self.head

        while node is not None:
            if node.value > max:
                max = node.value
            node = node.next

        return max

