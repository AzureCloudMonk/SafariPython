
def add(a, b):
    return a + b
    # if a != 1:
    #     return a + b

sum = add(2, 3)

sum += 10;

print(sum)

n = None
print(n is None)

sum = add("Hello", " World!")
print(sum)

# import zeller
# print(f"day of Jan 1 was {zeller.day_of_week(1, 1, 2021)}")

from zeller import day_of_week
print(f"day of Jan 1 was {day_of_week(1, 1, 2021)}")
print(f"day of Jan 1 was {day_of_week(day=1, month=1, year=2021)}")

def show_many(a, b, *args, **kwargs):
    print(f"a is {a}, b is {b}");
    print(f"c is {args} type is {type(args)}")
    for arg in args:
        print(f"> {arg}")
    print(f"kwargs is {kwargs}, type is {type(kwargs)}")
    for k, v in kwargs.items():
        print(f"{k} : {v}")

show_many(1, 2, 3, 4, 5, color="red", size="large")

values = [9, 8, "Albert"]
keyvals = {"color": "green", "size": "medium", "value": "high"}
show_many(1, 2, *values, **keyvals)

def has_default(a, b = "Hello world"):
    print(f"Messages are {a}, {b}")

has_default("Jim", "Bonjour")
has_default("Albert")

print("Hello", "everyone", sep="--", end="")
print("world")