def angry_professor(k, a):
    on_time = 0
    for arrival in a:
        if arrival <= 0:
            on_time += 1
    return "YES" if on_time >= k else "NO"

