def picking_numbers(a):
    sub_len = 0
    max_len = 0
    sub_more = []
    sub_less = []

    for i in range(len(a)):
        sub_more.append(a[i])
        sub_less.append(a[i])
        for j in range(0, len(a)):
            if j != i:
                if abs(a[i] - a[j]) <= 1 and a[j] > a[i]:
                    sub_more.append(a[j])
                elif abs(a[i] - a[j]) <= 1 and a[j] < a[i]:
                    sub_less.append(a[j])
                elif abs(a[i] - a[j] <= 1) and a[i] == a[j]:
                    sub_less.append(a[j])
                    sub_more.append(a[j])
        sub_len = max(len(sub_less), len(sub_more))
        if sub_len > max_len:
            max_len = sub_len
        sub_more = []
        sub_less = []
    return max_len


