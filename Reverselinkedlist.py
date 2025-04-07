class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyNode:
    def __init__(self):
        self.head = None

    def appenditem(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(item)

    def show(self):
        if self.head is not None:
            curr = self.head
            while curr:
                print(curr.data, end = ' ')
                curr = curr.next

    def reverse(self):
        if self.head is not None:
            curr = self.head
            head = curr
            temp = None
            while curr:
                newnode = curr.next
                curr.next = temp
                temp = curr
                curr = newnode
            return temp.data



s = SinglyNode()
s.appenditem(1)
s.appenditem(2)
s.appenditem(3)
s.appenditem(4)
s.appenditem(5)
s.appenditem(6)
s.appenditem(7)
s.appenditem(8)
s.appenditem(8)
s.show()
print()
x = s.reverse(s)
s.show()