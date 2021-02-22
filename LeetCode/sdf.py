#!/bin/python3

import sys


class AddingStack:
    def __init__(self) -> None:
        self.top = None
        self.count = 0
        self.mini = None

    def push(self, v: int) -> None:
        # Complete the function below

        if v < self.mini:
            temp = (2*v)-self.mini
            new_num = AddingStack(temp)
            new_num.next = self.top
            self.top = new_num
            self.mini = v
        else:
            new_num = AddingStack(v)
            new_num.next = self.top
            self.top = new_num
        print("{}".format(v))
        raise Exception("push not implemented")

    def pop(self) -> None:
        # Complete the function below
        if self.top is None:
            print("Empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.mini:
                self.mini = ((2*self.mini)-removedNode)
        raise Exception("pop not implemented")

    def inc(self, i: int, v: int) -> None:
        # Complete the function below
        if self.top is None:
            k = min(i-1, self.top)
            self.inc[k] += v

        raise Exception("inc not implemented")

    def empty(self) -> bool:
        # Complete the function below
        if self.top == None:
            return "EMPTY"
        raise Exception("empty not implemented")

    def peek(self) -> int:
        # Complete the function below
        if self.top is None:
            print("EMPTY")
        else:
            if self.top.v < self.mini:
                print("Top Element in Stack is : {}".format(self.mini))
            else:
                print("Top Element in Stack is: {}".format(self.top.v))
        raise Exception("peek not implemented")

    def sum(self) -> int:
        # Complete the function below
        if self.top is None:
            self.top = AddingStack(self.top.next)
            self.mini = self.top.next
        else:
            addedNode = self.top.v
            self.top.v = addedNode+1
            print(self.top.value)
            addedNode1 = self.mini
            self.mini = addedNode1+1
            print(self.mini)
        raise Exception("sum not implemented")


if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    stack = AddingStack()
    while operations_i < operations_cnt:
        try:
            operation = str(input())
        except:
            continue
        operations_i += 1

        commands = operation.split()
        if commands[0] == "push":
            stack.push(int(commands[1]))
        elif commands[0] == "pop":
            stack.pop()
        elif commands[0] == "inc":
            stack.inc(int(commands[1]), int(commands[2]))

        if stack.empty():
            print("EMPTY")
        else:
            print(stack.peek(), stack.sum())
