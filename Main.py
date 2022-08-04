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
    return self.top == self.size_of_stack-1


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    data = self.stack.pop()
    self.top -= 1
    return data


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
    data_stack = []
    top = -1
    status = False
    for i in expression:
      operands = []
      operator = ""
      try:
        num = int(i)
        status = True
      except:
        status = False
      if status:
        data_stack.append(int(i))
        top += 1
      elif i in ['+',"-","*","/","^"]:
        operands = []
        if len(data_stack) >=2:
          for j in range(2):
            data = data_stack.pop()
            operands.append(data)
          b ,a = operands
          if i == "+":
            data_stack.append(a+b)
          elif i == "-":
            data_stack.append(a-b)
          elif i == "/":
            data_stack.append(a/b)
          elif i == "*":
            data_stack.append(a*b)
          elif i == "^":
            data_stack.append(a^b)

    return len(data_stack) == 1 and len(expression) != 1
    #   return True

  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    associativity = {"(":'very_high',')':3,'^':2,'/':1,'*':1,'+':0,'-':0}
    data_stack = []
    top = -1
    status = False
    # print(expression)
    for i in expression:
      # print('i: '+i)
      # if i == "-":
        # print('- found!!!')
      # if i in ['+','*','/','^','-']:
        # print('yeah an operator')
      operands = []
      operator = ""
      try:
        num = int(i)
        status = True
      except:
        status = False
      if status:
        data_stack.append(int(i))
        top += 1
      elif i in ['+',"-","*","/","^"]:
        # if associativity[i] > data_stack[-1]:
          # print('has high '+str(data_stack[-1]))
        operands = []
        # print('got '+i)
        if len(data_stack) >=2:
          # print(">= 2")
          for j in range(2):
            data = data_stack.pop()
            operands.append(data)
          # print(operands)
          b ,a = operands
          # print(i)
          if i == "+":
            # print(a+b)
            data_stack.append(a+b)
          elif i == "-":
            data_stack.append(a-b)
          elif i == "/":
            data_stack.append(a/b)
          elif i == "*":
            data_stack.append(a*b)
          elif i == "^":
            # print(f"{a} ^ {b} =",a**b)
            data_stack.append(a**b)
      # else:
        # print("No match")
      # print(data_stack)

    # print(data_stack)
    return data_stack[-1]
    # return data_stack[0]



# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
