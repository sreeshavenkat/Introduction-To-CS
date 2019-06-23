def both_positive(x, y):
    """
    This code should return True if both x and y are positive, but it's not working.
    Figure out what's wrong here and fix the bug!

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x and y > 0

def should_get_one_free(x, y):
	"""
	A store is having a buy one get one free sale, but should only offer this discount if
	the second item costs less than the first, and if the total cost of the items is under $20.

	Write a function that takes two numbers prices as input (representing the two item prices)
	and returns True if the second item (y) costs less than the first (x), and if the total cost of the items is under $20.
	You should not use if in your solution
	>>> should_get_one_free(65, 12)
    False
    >>> gets_discount(9, 70)
    False
    >>> gets_discount(10, 8)
    True
	"""
	"*** YOUR CODE HERE ***"

def is_factor(x, y):
    """ 
    Returns True if x is a factor of y, False otherwise.

    >>> is_factor(3, 6)
    True
    >>> is_factor(4, 10)
    False
    >>> is_factor(0, 5)
    False
    >>> is_factor(0, 0)
    False
    """
    "*** YOUR CODE HERE ***"

def is_equal(a, b):
    """ 
    This code should check if a and b are equal, but it's not working.
    Figure out what's wrong here and fix the bug!

    >>> is_equal(4, 2)
    False
    >>> is_equal(4, 4)
    True
    """
    if a = b:
        return True
    return False