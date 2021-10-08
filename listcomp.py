nums = list(range(1, 5))

doubled = [ y * 2 for y in nums ]
print(nums)
print(doubled)

# need a square root function
from math import sqrt
# generate numbers for "o" (opposite of a right triangle) in range 1-13 inclusive
# for each of those, generate values for "a" (adjacent side) in range 1 - one-less-than opposite side
# calculate the hypotenuse h and store it using the "walrus" assignment operator
# the colon-equals / walrus / assignment operator forms an expression that has the value that's assigned
# so we can continue to compute using it
# then test to see if that hypotenuse value is a perfect integer, and if (and only if) it is
# then we put the resulting triplet of o, a, and h into the resulting list
# result a small set of perfect integer sided right-angled triangles
triangles = [ (o, a, h) for o in range (1, 14) for a in range(1, o) if int(h := sqrt(o * o + a * a)) == h ]
print(triangles)
