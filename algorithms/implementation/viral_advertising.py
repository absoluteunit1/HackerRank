def viral_advertising(n):
    recipients = 5
    liked = recipients//2
    shared = liked*3
    cumalitive = liked
    for day in range(2, n + 1):
        liked = shared//2
        cumalitive += liked
        shared = liked*3
    return cumalitive
