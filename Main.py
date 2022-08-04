class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return self.top == -1


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    self.top -= 1
    return self.stack.pop()


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    self.stack.append(operand)
    self.top += 1


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    operators = []
    operands = []
    for i in expression:
      if i.isdigit():
        operands.append(i)
      else:
        operators.append(i)

    status = len(operators) + len(operands) == len(expression) and len(operands)-1 == len(operators) and expression[0].isdigit() and expression[1].isdigit()
    return status



  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    for i in expression:
      if i.isdigit():
        self.push(int(i))
      elif i in ["+","-","*","/","^"]:
        if i == "+":
          b, a = self.pop(),self.pop()
          self.push(a+b)
        elif i == "-":
          b, a = self.pop(),self.pop()
          self.push(a-b)
        elif i == "*":
          b, a = self.pop(),self.pop()
          self.push(a*b)
        elif i == "/":
          b, a = self.pop(),self.pop()
          self.push(a//b)
        elif i == "^":
          b, a = self.pop(),self.pop()
          self.push(a**b)

    return self.pop()


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
