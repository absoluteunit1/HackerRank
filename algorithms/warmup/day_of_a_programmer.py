def day_of_a_programmer(year):
    # leap year date = Sep. 12
    # non leap year date = Sep. 13
    if year >= 1700 and year <= 1917:
        if year%4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year >1918 and year <= 2700:
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year == 1918:
        return f"26.09.{year}"



