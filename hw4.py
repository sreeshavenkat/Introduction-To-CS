def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """
    Returns the piecewise function h where:

    h(x) = f(x) if x < b, else g(x)

    >>> abs_value = piecewise(square, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"

def repeated(f, n):
    """
    Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    "*** YOUR CODE HERE ***"

