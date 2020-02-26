def migratory_birds(arr):
    ar = sorted(arr)
    my_dict = {i:ar.count(i) for i in ar}
    return max(my_dict, key=my_dict.get)
    