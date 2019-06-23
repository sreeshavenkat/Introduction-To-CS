from operator import add

def square(x):
	return x * x

def double(x):
	return x + x

def mystery(z):
	add(square(double(z)), 1)

def a(foo):
	return -foo

def b(foo):
	print(foo)

def bar(foo):
	return foo

def foo(bar):
	return bar(bar)

def determine_output():
	"""
	Calculate the values for each expression below by hand.
	You can check your work by running the following command from your terminal:
	>>> python hw3.py
	"""
	# Question 1
	x = 6
	assert square(x) == "YOUR ANSWER HERE"
	assert max(pow(2, 3), square(-5)) - square(4) == "YOUR ANSWER HERE"
	
	# Question 2
	assert mystery(4) == "YOUR ANSWER HERE"
	assert mystery(-1) == "YOUR ANSWER HERE"

	# Question 3
	assert a(4) == "YOUR ANSWER HERE"
	assert b(-4) == "YOUR ANSWER HERE"

	hello = a(4)
	goodbye = b(-4)
	assert hello + 1 == "YOUR ANSWER HERE"
	assert goodbye + 1 == "YOUR ANSWER HERE"

	# Question 4
	# What would happen if we called foo(4)? Write your answer below:
	# "YOUR ANSWER HERE"

	print("CONGRATS! You passed all the tests")

determine_output()