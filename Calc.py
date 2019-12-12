from operator import add, mul # modula

ASCII_ZERO = 48 # ascii code for '0'
ASCII_NINE = 57 # ascii code for '9'
LEFT_PARENTHESIS = '('
RIGHT_PARENTHESIS = ')'
OPERATORS = "()+-*/^!" # string containing the operators

def fac(x):
    """
    Calculate the factorial of the input integer x (recursion)
    Taken from previous hw4, completely written by me.

    Returns : int
        factorial of the integer x
    output : 
        -------
    """
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * fac(x - 1)

def exp(power, base):
    """
    Calculate the exponential of the base with given power (recursion)
    Taken from previous hw4, completely written by me.

    Returns : int
        integer that represent final output
    output : 
        -------
    """
    if (base == 0):
        return 0
    elif (power == 0):
        return 1
    elif (power == 1):
        return base
    else:
        return base * exp(power - 1, base) 

div = lambda x, y: int(y / x) # divide y by x

sub = lambda x , y: int(y - x) # subtract x from y

# if a character is an operator, return boolean indicating whether is operator
is_operator = lambda character: character in OPERATORS 

def is_digit(character):
    """
    check if a character is an digit
    original function 

    Returns : boolean
        True for digits, False otherwise
    output : 
        -------
    """
    if ASCII_NINE >= ord(character) >= ASCII_ZERO:
        return True
    else:
        return False

def is_valid(character):
    """
    check if a character is a valid input
    original function 

    Returns : boolean
        True for valid input, False otherwise
    output : 
        -------
    """
    return is_operator(character) or is_digit(character)

def decin(expression):
    """
    read decimal number until operator is detected
    original function 

    Returns : string
        substring for decimal number
    output : 
        -------
    """
    output = ""
    for char in expression:
        if is_digit(char):
            output = output + char # append output string
        else:
            break
    return output

def remove_str(expression, substring):
    """
    remove first substring from expression
    original function 

    Returns : string
        substring for remaining string
    output : 
        -------
    """
    return expression[len(substring):]

# the function arrays, from cse 12 hw4
functions = [None, None, add, sub, mul, div, exp, fac]

class Calculator():
    """
    class Calculator
    It has functions that can convert expression into postfix and evaluate it.
    It also contains a few helper methods to accomplish it.
    original function 

    """

    def evaluate(self, stack1):
        """
        evaluate the postfix expression
        taken prom previous hw, completely written by me

        Returns : int
            the final result of the expression
        output : 
            -------
        """
        stack2 = [] # empty stack for operation

        # reverse stack1 to stack2
        while True:
            if not stack1:
                break
            item = stack1.pop()
            stack2.append(item)

        # if stack2 is empty, return false
        if not stack2:
            return False

        # evaluation of the postfix expression
        while stack2:
            item = stack2.pop()

            # when item is an operator, get its index
            if is_operator(item):
                operator = item
                operator_index = OPERATORS.find(operator)

                # factorial case
                if operator == '!':
                    item = int(stack1.pop())
                    stack1.append(functions[operator_index](item))

                # all other operations
                else:
                    item = int(stack1.pop()) # casting to int
                    item2 = int(stack1.pop()) # casting to int
                    stack1.append(functions[operator_index](item, item2))

            # push item to stack1 if it's a number
            else:
                stack1.append(item)

        return stack1.pop() # return the final result

    def intopost(self, expression):
        """
        convert string expression into postfix
        taken prom previous hw, completely written by me

        Returns : list
            the list containing the postfix expression
        output : 
            -------
        """
        stack1 = []
        stack2 = []

        while len(expression):
            character = expression[0] # char character

            if character == " ":
                expression = remove_str(expression, character)
                continue

            if is_digit(character):
                character = decin(expression) # read the number and assign back
                expression = remove_str(expression, character)
                stack1.append(character)
                continue

            # when left parenthesis is detected
            elif character == LEFT_PARENTHESIS:
                stack2.append(character)

            # when right parenthesis is encountered
            # dumping the operators to stack1 until encountering '('
            elif character == RIGHT_PARENTHESIS:
                while True:
                    item = stack2.pop()
                    if (item == LEFT_PARENTHESIS):
                        break
                    stack1.append(item)

            # operator case
            else:
                operator1 = character
                operator2 = ""

                while True:
                    # when stack2 is empty
                    if not stack2:
                        stack2.append(character)
                        break

                    operator2 = stack2[len(stack2) - 1] # topping the stack

                    # push it to stack1 if the item is greater
                    if self.precedence(operator1) > self.precedence(operator2):
                        stack2.append(operator1)
                        break
                    # push operator 2 to stack1
                    else:
                        operator2 = stack2.pop()
                        stack1.append(operator2)

            expression = remove_str(expression, character) # remove the char
            # end of the while loop

        # push the remaining item from stack2 to stack1
        while stack2:
            item = stack2.pop()
            stack1.append(item)

        return stack1 # return stack1 with postfix expression


    def precedence(self, operator):
        """
        get the precedence of the operator
        original function

        Returns : int
            the precedence of the operator
        output : 
            -------
        """
        index = OPERATORS.find(operator)
        if 1 >= index >= 0:
            return 1
        elif 3 >= index >= 2:
            return 2
        elif 5 >= index >= 4:
            return 3
        elif index == 6:
            return 4
        elif index == 7:
            return 5


    def get_operator(self, index):
        """
        get the operator from operator string
        original function

        Returns : string
            the operator
        output : 
            -------
        """
        return OPERATORS[index]
    # end of class Calculator
