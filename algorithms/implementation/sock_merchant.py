def sock_merchant(n, ar):
    sock_counter = {i: ar.count(i) for i in ar}
    pairs = 0
    for key, value in sock_counter.items():
        if value > 1:
            if value%2 == 0:
                pairs += value/2
            else:
                pairs += (value-1)/2
    return f"{pairs:.0f}"

