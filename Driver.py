import Calc


#creating the calculator object
myCalculator = Calc.Calculator()


def isvalid_exp(expression):
	"""
	evaluate if an expression contains invalid character
	my original

	Returns : boolean
		True for valid, False otherwise
	output :
		-------
	"""
	if not expression:
		return False # if the expression is empty
	for i in expression:
		# delegate to is_valid function
		if Calc.is_valid(i) or i == " ":
			continue
		else:
			return False
	return True # return True when the loop is over


def prompt():
	"""
	prompt user for entry
	my original 
	
	Returns :
		-------
    output : string
        prompting messages
    """
	print("Welcome to Leo's calculator. Follow instructions to continue")
	print("Press (e)xit to exit")
	while True:
		print()
		expression = input("Please enter a valid expression:  ")
		if expression == "e":
			return expression
		print()
		# when invalid character detected, prompt again
		if not isvalid_exp(expression):
			print("Invalid character entered. Please try again!!!", '\n')
			continue
		break

	# call Calculator method
	post = myCalculator.intopost(expression)
	post_str = " ".join(post) # convert list to string with space
	# print out the post fix expression
	print("The postfix conversion of your expression is:", post_str, '\n')

	result = myCalculator.evaluate(post)
	# print out result
	print("The expression that you entered evaluates to:", result)

	print() # newline


def main():
	"""
    main driver that keep the program running
	my original function

    Returns : 
        -------
    output : string
        prompting messages
    """
	while True:
		result = prompt()
		if result == 'e':
			return
		# continuation of program
		print("Do you want to continue using this calculator?")
		user_input = input("Please enter your choice (y)es or (n)o:  ")
		# continue if user enters y, terminate otherwise
		if user_input == 'y':
			print()
			continue
		else:
			break

