
x = 4
while x > 0:
    # pass # pass gives structural integrity when you have nothing else to say!!
    print(x)
    x -= 1

print("all done")

x = 1
print(x)
if x:
    print("x is Truthy")
    print(f"its value is {x}")
else:
    print("x is Falsy")

print("----------------")
x = 5
while x > 0:
    print(x)
    x -= 1;
    if x == 1:
        break
else:
    print("in the else!!!")

