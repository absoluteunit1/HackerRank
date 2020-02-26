def between_two_sets(a, b):
    numsBetween = set()
    for i in range(1, max(b) + 1):
        if all(i % num_a == 0 for num_a in a) and all(num_b % i == 0 for num_b in b):
            numsBetween.add(i)
    return len(numsBetween)
