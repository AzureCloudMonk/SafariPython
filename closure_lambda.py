
def add(a, b):
    """
    This is the documentation for my amazing add function
    :param a: the first number to be added
    :param b: the number to add to the first
    :return: the sum
    """
    return a + b

sum = lambda a, b : a + b

sum2 = add

print(add(3, 4))
print(sum(5, 7))

print(sum2(9, 9))

def make_adder(v):
    return lambda b : v + b

plus_two = make_adder(2)

plus_four = make_adder(4)

print(plus_two(6))
print(plus_four(9))

print(add.__doc__)


# Exceptions
# Classes
# Inheritance