def circular_array_rotation(a, k, queries):
    new_arr = a[-k:] + a[:-k]
    return [new_arr[i] for i in queries]

