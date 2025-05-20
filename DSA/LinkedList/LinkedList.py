# from DSA.Sorting.LinkedList import LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        print(new_node.data)
        print(new_node.next)
        if not self.head:
            self.head = new_node
            print("head")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next

    # Display all the nodes in the Linked List

    def display(self):
        temp = self.head
        print("51",temp.data)
        print("52",temp.next)
        while temp:
            print(temp.data, "->")
            temp=temp.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.add_at_beginning(5)
ll.append(30)
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None
