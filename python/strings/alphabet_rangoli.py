import string

def print_rangoli(size):

    letters = string.ascii_lowercase[0:size]
    lines = size*2 - 1
    lineLength = lines*2 - 1

    for i in range(lines):
        for j in range(lineLength):
            if j%2 == 0:
                print(letters[-1:], end="")
            else:
                print("-", end="")
        print()


# printing a multiplicaton table of numbers 
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j, end="-") if j != 5 else print(i*j, end="")  # python automatically ends with \n and goes to next line after a print statement; end specifies what to end the print statement with 
#     print()

print_rangoli(3)
print_rangoli(5)