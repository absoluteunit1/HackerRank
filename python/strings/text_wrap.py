import textwrap

def text_wrap(string, max_width):
    wrapped_string = ""
    count = 0
    for letter in string:
        if count%max_width == 0 and count != 0:
            wrapped_string += "\n"
        count += 1
        wrapped_string+=letter
    return wrapped_string

# Other submissions

def text_wrap(string, max_width):
    return textwrap.fills(string, max_width)
    