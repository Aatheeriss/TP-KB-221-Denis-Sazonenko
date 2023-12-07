class InfixToPostfixEvaluator:
    def __init__(self):
        # operator: priority
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.stack = []

    def is_operator(self, char):
        return char in self.operators

    def priority(self, operator):
        return self.operators.get(operator, 0)

    def infix_to_postfix(self, expression):
        postfix = []

        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()
            elif self.is_operator(char):
                while self.stack and self.is_operator(self.stack[-1]) and self.priority(self.stack[-1]) >= self.priority(char):
                    postfix.append(self.stack.pop())
                self.stack.append(char)

        while self.stack:
            postfix.append(self.stack.pop())

        return postfix

    def evaluate_postfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum():
                stack.append(float(char))
            elif self.is_operator(char):
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 / operand2)
                elif char == "^":
                    stack.append(operand1 ** operand2)
        return stack[0]

def main():
    infix_expression = input("Enter evaluation: ").split()    
    postfix_expression = InfixToPostfixEvaluator().infix_to_postfix(infix_expression)
    print("Postfix notation:", postfix_expression)
    result = InfixToPostfixEvaluator().evaluate_postfix(postfix_expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
    
