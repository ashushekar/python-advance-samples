"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always
evaluate to a result and there won't be any divide by zero operation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        len_tokens = len(tokens)
        if 0 == len_tokens:
            return 0

        # python has no stack, so we have to simulate it
        nums_stack = []

        for i in range(0, len_tokens):
            token = tokens[i]
            # consider negative number, so shouldn't decide by the first char, but last char
            last_ch = token[len(token) - 1]
            if last_ch >= '0' and last_ch <= '9':
                nums_stack.append(int(token))
            else:
                right = nums_stack.pop()
                left = nums_stack.pop()
                if '+' == token:
                    result = left + right
                elif '-' == token:
                    result = left - right
                elif '*' == token:
                    result = left * right
                else:
                    sign = 1 if (left >= 0 and right >= 0) or (left <= 0 and right <= 0) else -1
                    result = abs(left) // abs(right) * sign
                nums_stack.append(result)

        return nums_stack.pop()