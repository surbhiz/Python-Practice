class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)


class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    # Method to check if Stack is Empty or not

    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return "Empty"
        else:
            # If top not equal to None then stack is empty
            return False

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum2
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("{}" .format(value))

    def pop(self):
        if self.top is None:
            print("Empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                self.minimum = ((2 * self.minimum) - removedNode)

    def incrementval(self):
        if self.top is None:
            self.top = Node(self.top.next)
            self.minimum = self.top.next

        else:
            addednode = self.top.value
            self.top.value = addednode+1
            print(self.top.value)
            addednode1 = self.minimum
            self.minimum = addednode1+1
            print(self.minimum)


stack = Stack()

stack.push(4)
stack.pop()
stack.incrementval(3, 1)
stack.push(3)
stack.push(5)
stack.push(2)
