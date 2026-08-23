# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# STACK 
class Stack:
    def __init__(self):
        self.top = None

    # PUSH operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed into stack.")

    # POP operation
    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return
        temp = self.top
        print(temp.data, "popped from stack.")
        self.top = self.top.next

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        temp = self.top
        print("Stack:", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# QUEUE 
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ENQUEUE operation
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(value, "enqueued into queue.")

    # DEQUEUE operation
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return
        temp = self.front
        print(temp.data, "dequeued from queue.")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        temp = self.front
        print("Queue:", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

#--- MAIN PROGRAM ---

# Stack operations
print("----- STACK OPERATIONS -----")
s = Stack()
s.push(20)
s.push(11)
s.push(17)
s.display()
s.pop()
s.display()

# Queue operations
print("\n----- QUEUE OPERATIONS -----")
q = Queue()
q.enqueue(11)
q.enqueue(20)
q.enqueue(17)
q.display()
q.dequeue()
q.display()