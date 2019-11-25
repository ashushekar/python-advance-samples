"""
Check for balanced parentheses in Python
Given an expression string, write a python program to find whether
a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced
"""

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def checkstring(str):
    stack = []
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack) == 0:
        return "Balanced"


string = "[{}{})(]"
print("{}: {}".format(string, checkstring(string)))