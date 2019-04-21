def days_in_month(month, year=1):
    if month == 9 or month == 4 or month == 6 or month == 11:
        return 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 != 0:
                return 29
            elif year % 400 == 0:
                return 29
            else:
                return 28

        else:
            return 28
    else:
        return 31


def days_in_year(year):
    days = 0
    for month in range(1, 13):
        days += days_in_month(month, year)
    return days


def day(d, m, y):
    days_of_the_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    days = 0
    for i in range(1900, y):
        days += days_in_year(i)
    for i in range(1, m):
        days += days_in_month(i, y)
    days += 1 - d
    day = days_of_the_week[days % 7]
    return day


count = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day(1, month, year) == "sun":
            count += 1

print(count)
