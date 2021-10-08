from random import random

try:
    value = random()
    print(value)
    if value > 0.5:
        raise ValueError("that's a big value, I can't handle it")
    if value > 0.25:
        b = 0
        print(value / b)
except ZeroDivisionError as zde:
    print(f"that broke, division by zero {zde}" )
except ValueError as ve:
    print(f"that broke, bad value {ve}")
finally:
    print("I should always run this")

# except:
#     print("that broke")

print("--------------------")

# "with" structure does NOT handle exceptions, it ONLY
# closes the resources...
with open("text.txt", "r") as input, open("copy.txt", "w") as output:
    for line in input:
        print("> " + line, end="")
