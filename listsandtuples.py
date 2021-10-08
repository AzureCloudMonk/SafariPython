
names = ["Fred", "Jim", "Sheila"]
print(names)
print(type(names))
print(names[0])
print(names[-1])

tennumbers = range(1, 10)
print(type(tennumbers))
print(tennumbers)
numbers = list(tennumbers)
print(numbers)
print(numbers[0:5:2])
print(numbers[-1:0:-1])
print(numbers[::-1])

t = 1, 2, 3
t = (1, 2, 3)
print(t)
print(type(t))
print(t[0:2])
a, b = t[0:2]
# a, b = t[0:3]  # NOPE, mismatched number of elements
print(a)
print(b)
print(t[0])
t[0] = 99
print(t[0])
