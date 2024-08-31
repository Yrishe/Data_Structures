'''
Implementing a queue with linked lists

1. Define the Node class:
    Each node in the linked list will have two attributes: data to store
    the value and next to point to the next node in the list.

2. Define the Queue class:
    The queue class will maintain two pointers: front and rear.
    The front pointer will point to the first node (oldest node) in the queue.
    And the rear pointer will point to the last node (newest node) in the queue.
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None

    def is_empty(self):
        return self.front is None

    '''
    If queue is empty then sets both front and rear to new node, otherwise
    update the next pointer of the current rear node and moves the rear pointer to the new node.
    '''
    
    # Enqueue at the end 
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = self.new_node 
            return 
        self.rear.next = new_node 
        self.rear = new_node 

    '''
    Dequeue removes the front node from the queue and returns its data, 
    If the queue is empty it raises the IndexError
    '''

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Dequeue from an empty queue')
        temp = self.front 
        self.front = temp.next 
        if self.front is None:
            self.rear = None
        return temp.data 

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            temp = self.front
            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next 
            print('None')

'''
The implementation ensures that both enqueue and dequeue operations are efficient, running in O(1) time complexity.
'''

