#!/usr/bin/python

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return 0
        stack = []
        def isOpenrand(s):
            return s == '+' or s == '-' or s == '*' or s == '/'
        for i in range(len(tokens)):
            if isOpenrand(tokens[i]) == False:
                stack.append(int(tokens[i]))
                continue
            if len(stack) < 2:
                return 0
            num2 = stack.pop()
            num1 = stack.pop()
            if tokens[i] == '+':
                stack.append(num1 + num2)
            elif tokens[i] == '-':
                stack.append(num1 - num2)
            elif tokens[i] == '*':
                stack.append(num1 * num2)
            elif tokens[i] == '/':
                stack.append(int(num1 / num2))
        return stack.pop()

test = Solution()
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
