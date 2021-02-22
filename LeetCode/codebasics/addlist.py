class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given node must be in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):

       # 1. Create a new node
       # 2. Put in the data
       # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()

# Insert 6.  So linked list becomes 6->None
llist.append(6)

# Insert 7 at the beginning. So linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.append(4)

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)

print('Created linked list is:')
llist.printList()
