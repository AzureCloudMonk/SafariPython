# from __future__ import braces
# Python has no braces, but does have a sense of humor

names = {"Fred": "Jones", "Jim": "Smith"}
print(names)
print(type(names))
print(names["Fred"])

print("Fred" in names)
#  test for containing a key before access, or it breaks!
# print(names["Alan"])

names["Alan"] = "Williams"

print(names.keys())
print(names.values())
print(names.items())

for k in names:
    print(k)
print("--------------")
for k in names.keys():
    print(f"key= {k} : value = {names[k]}")


print("--------------")
for tup in names.items():
    print(f"key= {tup[0]} : value = {tup[1]}")

print("--------------")
for k, v in names.items():
    print(f"key= {k} : value = {v}")

for x in range(1, 10, 2):
    print(x)
    