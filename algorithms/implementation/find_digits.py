def find_digits(n):
    m = str(n)
    count = 0
    for digit in m:
        if digit != '0' and n%(int(digit)) == 0:
            count += 1
    return count



















