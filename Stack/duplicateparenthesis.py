"""
Given a balanced expression, find if it contains duplicate parenthesis or not.
A set of parenthesis are duplicate if the same subexpression is surrounded by
multiple parenthesis.

Time complexity is O(n)
"""


def findDuplicateparenthesis(str):
    stack = []
    for i in str:
        if i == ')':
            top = stack.pop()
            counter = 0
            while top != '(':
                counter += 1
                top = stack.pop()
            if counter < 1:
                return True
        else:
            stack.append(i)

    return False


# Driver Code
if __name__ == "__main__":
    # input balanced expression
    string = "((a+b)+(c+d))"

    if findDuplicateparenthesis(string) == True:
        print("Duplicate Found")
    else:
        print("No Duplicates Found")