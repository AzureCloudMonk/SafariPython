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


