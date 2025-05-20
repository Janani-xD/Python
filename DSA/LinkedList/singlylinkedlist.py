from idlelib.configdialog import tracers


class SinglyNode:
    def __init__(self, val, nextaddr=None):
        self.val = val
        self.next = nextaddr

    def __str__(self):
        return str(self.val)

    def traverse(self, Head):# O(n)
       while Head:
            print(Head)
            Head = Head.next

    def display(self, Head):# O(n)
        elements = []
        while Head:
            elements.append(str(Head.val))
            Head = Head.next
        print('->'.join(elements))

    def search(self, Head, val): # O(n)
        while Head:
            if val == Head.val:
                return True
            Head = Head.next
        return False

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
Head.next = A
A.next = B
B.next = C
print(Head.display(Head))
print("Search Element : ", 10, Head.search(Head, 7))

