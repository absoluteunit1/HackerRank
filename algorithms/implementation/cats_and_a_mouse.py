def cat_and_mouse(x, y, z):
    if abs(z - x ) > abs(z - y):
        return 'Cat B'
    elif abs(z - y) > abs(z - x):
        return 'Cat A'
    else:
        return 'Mouse C'
