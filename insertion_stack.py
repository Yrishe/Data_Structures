'''
Insertion applied on stack and respecting the following 
rules: 
    •	push(item): Adds an item to the top of the stack.
	•	pop(): Removes and returns the top item of the stack.
	•	peek(): Returns the top item of the stack without removing it.
	•	is_empty(): Checks if the stack is empty.

Here is the step-by-step approach to implement it:
	1.	Initialization: Start with the original stack and an empty auxiliary stack.
	2.	Pop and Sort: Repeatedly pop elements from the original stack and insert them in sorted order into the auxiliary stack.
	3.	Insert into Auxiliary Stack: Use the auxiliary stack to maintain sorted order by temporarily moving elements back to the original stack when necessary.
	4.	Transfer Back: Once all elements are sorted in the auxiliary stack, move them back to the original stack.
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def insertion_sort_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        current = stack.pop()

        #Move elements from aux_stack back to stack if they are greater than current
        while not aux_stack.is_empty() and aux_stack.peek() > current:
            stack.push(aux_stack.pop())

        #Push the current element into the correct position in aux_stack
        aux_stack.push(current)

    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())

if __name__ == "__main__":
    stack = Stack()
    elements = [34, 3, 31, 98, 92, 23]
    for elem in elements:
        stack.push(elem)

    print("Original Stack:", stack)
    insertion_sort_stack(stack)
    print("Sorted Stack:", stack)

