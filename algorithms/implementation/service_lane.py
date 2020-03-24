# My solution
def serviceLane(width, cases):
    max_car_widths = []
    for index in cases:
        max_car_widths.append(min(i for i in width[index[0]: index[1] + 1]))
    return max_car_widths

