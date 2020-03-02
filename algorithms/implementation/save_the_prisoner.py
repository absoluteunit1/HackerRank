# n = number of prisoners
# m = the number of sweets
# s = chair number to begin passing out treats from

# Brute force: works only for small number of prisoners
# while m != 1:
#         if s == n:
#             s = 0
#         m -= 1
#         s += 1
#     return s

def save_the_prisoner(n, m, s):
    # still working on it