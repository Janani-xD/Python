class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)
# Display O(n)
    def display(self, Head):
        elements = []
        while Head:
            elements.append(str(Head.val))
            Head = Head.next
        print("<->".join(elements))

    def insert_at_beginning(self, head, tail, val):
        new_node = DoublyNode(val, next=head)
        head.prev = new_node
        return new_node, tail

    def insert_at_end(self, head, tail, val):
        new_node = DoublyNode(val, prev=tail)
        tail.next = new_node
        return head,new_node

head = tail = DoublyNode(1)
head1, tail1 = DoublyNode.insert_at_beginning(head,head=head, tail=tail, val = 3)
print(head.display(head))
