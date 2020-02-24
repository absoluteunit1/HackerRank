def viral_advertising(n):
<<<<<<< HEAD
    recipients = 5
    liked = recipients//2
    shared = liked*3
    cumalitive = liked
    for day in range(2, n + 1):
        liked = shared//2
        cumalitive += liked
        shared = liked*3
    return cumalitive
=======
    pass
>>>>>>> 7a8cf78b70dd16a87b3fe5578973bec74f86bb40
