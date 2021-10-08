x = 99  # also, binary 0b101011 0xCAFE
print(x)
print(type(x))

x = 99.9
print(x)
print(type(x))

x = 999999999999999999999999999999999999999999999999999999999999999999999999
print(x * x)

x = "hello"
print(x)
print(type(x))

x = 100
# print("Hello, the value is " + x)  # FAILS both elements must be str for concatenation!
print(f"Hello, the value is {x + 10}")
print("Hello, the value is " + str(x))

# operators ... fairly normal
a = 10
b = 3
print(a / b)  # "normal" division produces float results, even from int types
print(a // b)  # // is integer division

# raise to power operator **
print(2 ** 32)

# comparisons are defined by "dunder" methods in a class, __lt__
b = 2 < 3  # bool is a real type, but all types exhibit "truthy and falsy" behavior
print(type(b))
print(b)

if x:
    print("that's True!")

print(bool("Hello"))

h = "Hello"
h1 = "Hello"

print(h == h1)
print(h is h1)

print("------------")
h1 = "He"
h1 = h1 + "llo"
print(h == h1)  # delegates to __eq__ method
print(h != h1)  # delegates to __eq__ method
print(h is h1)

# x = 3
# print(3 is x)


# semicolons are legal, but unnecessary, unless you put
# multiple statements on a single line (yuk!)
a = 1; b = 2;
print(f"a is {a}, b is {b}")

a = 0xFF00
b = 0b10101010
print(a)
print(b)
print(a & b)
print(a | b)

# print(True & True)
# print(True | False)
print(True and True)
print(True or False)

# imports by PEP8 convention *should* be at the top of the file!!!
# from operator import xor
# print(xor(True, True))
# print(xor(True, False))
import operator
print(operator.xor(True, True))
print(operator.xor(True, False))

