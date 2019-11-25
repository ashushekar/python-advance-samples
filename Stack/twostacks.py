"""
Create a data structure twoStacks that represents two stacks. Implementation
of twoStacks should use only one array, i.e., both stacks should use the same
array for storing elements.
Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack

pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element
"""
import sys


class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, element):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = element
        else:
            print("Stack Overflow")
            sys.exit(1)

    def push2(self, element):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = element
        else:
            print("Stack Overflow")
            sys.exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow")
            sys.exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 -= 1
            return x
        else:
            print("Stack Underflow")
            sys.exit(1)


ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
