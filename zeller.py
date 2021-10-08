print("initializing zeller")
# Saturday = 0
def day_of_week(day, month, year):
    m, y = (month, year) if month > 2 else (month + 12, year - 1)
    return (day + (13 * (m + 1) // 5) + year + year // 4 - year // 100 + year // 400) % 7


# print(f"today is day number {day_of_week(8, 10, 2021)}")
# named argument passing (as distinct from positional)
print(f"today is day number {day_of_week(month=10, day=8, year=2021)}")

print("zeller initialized")
