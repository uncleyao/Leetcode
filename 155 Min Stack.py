__author__ = 'yyao'

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):
    def __init__(self):
        """
        initiate
        """
        self.stack = []
        self.min = 0

    def push(self,x):
        ##
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()


    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return sorted(self.stack)[0]
        else:
            return 0


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(4)
    minStack.push(5)
    minStack.push(1)
    minStack.push(3)
    assert minStack.getMin() == 1
    minStack.pop()
    minStack.pop()
    assert minStack.top() == 5
