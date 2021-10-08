
class date:
    def __init__(self, day, month, year):
        print("constructor...")
        self.day = day  # MUST use "self" at ALL TIMES
        self.month = month
        self.year = year

    def __str__(self):
        return f"a date with {self.day} / {self.month} / {self.year}"

    def __repr__(self):
        # return str(self)
        return self.__str__()

    def tomorrow(self):  # define a "regular method" without self?? it's kinda neither one thing nor the other
        self.day += 1  ## what about wrapping around the end of the month!!

    @staticmethod
    def is_leap_year(y):
        return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

    # def __

d = date(8, 10, 2021)  # we don't use "new"
print(d)
print(type(d))

# d.day = 8
# d.month = 10
# d.year = 2021

print(f"day is {d.day}")
print("the date renders as text as " + str(d))
d.tomorrow()
print(f"now it's tomorrow: {d}")

dates = [ date(1, 1, 2021), date(9, 10, 2011)]
print(f"the dates are {dates}")

print(f"2021 is leap? {date.is_leap_year(2021)}")
print(f"2020 is leap? {date.is_leap_year(2020)}")

class holiday(date):
    def __init__(self, day, month, year, name):
        print("constructing holiday...")
        super().__init__(day, month, year)
        self.name = name

    def __str__(self):
        return super().__str__() + " a holiday called " + self.name

h = holiday(1, 1, 2022, "new year's day")
print(f"holiday is {h}")