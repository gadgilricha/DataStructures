from Stacks import StackArray 
def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """
    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated""" 
    operandStack = StackArray(30)
    postfixList = []
    tokenList = infixexpr.split()
    precedence = {
    "^":4,
    "*":3,
    "/":3,
    "+":2,
    "-":2,
    "(":1
    }
    for token in tokenList:
        if is_valid(token):
            postfixList.append(token)
        else:
            if token == '(':
                operandStack.push(token)
            elif token == ')':
                top = operandStack.pop()
                while top != '(':
                    postfixList.append(top)
                    top  = operandStack.pop()
            else:
                while (operandStack.is_empty() == False) and (precedence[operandStack.peek()] >= precedence[token] and token != "^"):
                    postfixList.append(operandStack.pop())
                operandStack.push(token)
    while operandStack.is_empty() == False:
        postfixList.append(operandStack.pop())
    return " ".join(postfixList)
#6 * ( 3 + 2 )

def postfix_eval(postfixExpr):
    """Evaluate the postfix expression using Stacks, and return final answer """
    opStack = StackArray(30)
    tList = postfixExpr.split()

    for t in tList:
        if t in "0123456789":
            opStack.push(int(t))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = doMath(t,op1,op2)
            opStack.push(result)
    return opStack.pop()


def doMath(operator, op1, op2):
    """method to do math, according to the operator and numbers passed, returns answer"""
    if operator == "^": 
        return op2 ^ op1 #exponents handled from right to left
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        if op2 == 0:
            raise ValueError("Cannot divide by 0!") #raise value error if trying to divide by 0
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    else:
        return op1 - op2

def postfix_valid(postfixexpr):
    """Checks to see if the postfix expression is valid -- makes sure stack returns only one number, returns whether expression valid or not""" 
    expr = postfixexpr.split(" ")
    count = 0
    isvalid = True
    for i in expr:
        if is_valid(i):
            count += 1
        elif i == '+' or '-' or '*' or '/' or '^':
            count -= 2
            if count < 0:
                isvalid = False
            count += 1

    if count == 1 and isvalid:
        return True
    else:
        return False

def is_valid(str):
    """ensures validity of numbers given -- converts float to integer if needed"""
    try:
        float(str)
        return True
    except ValueError:
        return False




    



#se the split function to convert the input to a list of tokens
