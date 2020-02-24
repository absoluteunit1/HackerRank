def beatiful_days(i, j, k):
    beatifulDays = 0
    for day in range(i, j + 1):
        if (int(str(day)[::-1]) - day) % k == 0:
            beatifulDays += 1
    return beatifulDays
