# Stack Implementation using Fixed-size Array
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = [None] * self.capacity
    
    def push(self, item):
        if self.top >= self.capacity - 1:
            print("Stack Overflow: Cannot push", item)
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"Push: {item} -> Stack after push: {self.stack[:self.top+1]}")
    
    def pop(self):
        if self.top == -1:
            print("Stack Underflow: Cannot pop, stack is empty")
        else:
            item = self.stack[self.top]
            self.top -= 1
            print(f"Pop: {item} -> Stack after pop: {self.stack[:self.top+1]}")
            return item
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty: No element to peek")
        else:
            print(f"Peek: {self.stack[self.top]}")
            return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1

# Queue Implementation using Fixed-size Array
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.queue = [None] * self.capacity
    
    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print(f"Queue Overflow: Cannot enqueue {item}, the queue is full")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            print(f"Enqueue: {item} -> Queue after enqueue: {self.queue[self.front:self.rear+1]}")
    
    def dequeue(self):
        if self.front == (self.rear + 1) % self.capacity:
            print("Queue Underflow: Cannot dequeue, the queue is empty")
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            print(f"Dequeue: {item} -> Queue after dequeue: {self.queue[self.front:self.rear+1]}")
            return item
    
    def peek(self):
        if self.front == (self.rear + 1) % self.capacity:
            print("Queue is empty: No element to peek")
        else:
            print(f"Peek: {self.queue[self.front]}")
            return self.queue[self.front]
    
    def is_empty(self):
        return self.front == (self.rear + 1) % self.capacity

# Singly Linked List Implementation using Fixed-size Array
class SinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = -1
        self.list = [None] * self.capacity
    
    def insert(self, value):
        if self.size >= self.capacity:
            print("List is full: Cannot insert", value)
            return
        new_node = self.size
        self.list[new_node] = {'data': value, 'next': -1}
        
        if self.head == -1:
            self.head = new_node
            print(f"Insert: {value} -> List after insert: {self.print_list()}")
        else:
            last = self.head
            while self.list[last]['next'] != -1:
                last = self.list[last]['next']
            self.list[last]['next'] = new_node
            print(f"Insert: {value} -> List after insert: {self.print_list()}")
        
        self.size += 1
    
    def delete(self, value):
        current = self.head
        prev = -1
        
        while current != -1 and self.list[current]['data'] != value:
            prev = current
            current = self.list[current]['next']
        
        if current == -1:
            print(f"Value {value} not found in list")
            return
        
        if prev == -1:
            self.head = self.list[current]['next']
        else:
            self.list[prev]['next'] = self.list[current]['next']
        
        self.list[current] = None
        self.size -= 1
        print(f"Delete: {value} -> List after delete: {self.print_list()}")
    
    def search(self, value):
        current = self.head
        while current != -1:
            if self.list[current]['data'] == value:
                print(f"Search: {value} found in list")
                return True
            current = self.list[current]['next']
        print(f"Search: {value} not found in list")
        return False
    
    def print_list(self):
        result = []
        current = self.head
        while current != -1:
            result.append(self.list[current]['data'])
            current = self.list[current]['next']
        return " -> ".join(map(str, result)) + " -> None"

# Example usage:
print("=== Stack Operations ===")
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.peek()
stack.pop()

print("\n=== Queue Operations ===")
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()

print("\n=== Singly Linked List Operations ===")
sll = SinglyLinkedList(5)
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.search(20)
sll.delete(20)
sll.search(20)
