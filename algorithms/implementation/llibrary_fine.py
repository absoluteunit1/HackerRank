from datetime import date

# My solution. Realized that I probably didn't need the datetime module here...

def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date     = date(y1, m1, d1)
    due_date        = date(y2, m2, d2)

    if return_date <= due_date:
        return 0

    elif due_date.year == return_date.year and due_date.month == return_date.month and return_date.day > due_date.day:
        days_overdue = int(return_date.day) - int(due_date.day)
        return 15*days_overdue

    elif due_date.year == return_date.year and return_date.month > due_date.month:
        months_overdue = int(return_date.month) - int(due_date.month)
        return 500*months_overdue

    else:
        return 10000

