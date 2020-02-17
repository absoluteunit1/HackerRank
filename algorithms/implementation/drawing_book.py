def page_count(n, p):
    f_page_turns, b_page_turns = 0, 0
    current_page = 1
    b_current_page = n

    # going forwards

    while(current_page != p):
        current_page += 1
        if current_page%2 == 0:
            f_page_turns += 1

    # going backwards
    if n%2 == 1:
        while(b_current_page != p):
            b_current_page -= 1
            if b_current_page%2 == 1:
                b_page_turns += 1
    else:
        while(b_current_page != p):
            b_current_page -= 1
            if b_current_page%2 == 1:
                b_page_turns += 1

    return min(f_page_turns, b_page_turns)

