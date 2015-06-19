#!/usr/bin/python

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def operand(self, s):
        return s == '+' or s == '-' or s == '*' or s == '/'
    
    def calculate(self, s, num1, num2):
        if s == '+':
            return num1 + num2
        elif s == '-':
            return num1 - num2
        elif s == '*':
            return num1 * num2
        elif s == '/':
            if num1 * num2 < 0:
                return -((-num1) / num2 )
            return num1 / num2

    def evalRPN(self, tokens):
        s = 0
        stack = []
        for i in range(len(tokens)):
            if not self.operand(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                if len(stack) < 2:
                    return 0
                num2 = stack.pop()
                num1 = stack.pop()
                s = self.calculate(tokens[i], num1, num2)
                stack.append(s)
        return stack.pop()


test = Solution()
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
