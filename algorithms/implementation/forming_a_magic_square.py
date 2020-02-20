# not finished! still working on it
def forming_magic_square(s):
    rows = []
    cols = []
    sums = {}


    cost = 0
    row_sum = 0
    col_sum = 0
    diag_sum1 = 0
    diag_sum2 = 0

    # find sums of rows and columns
    for i in range(len(s)):
        for j in i:
            row_sum += s[i][j]
            col_sum += s[j][i]
        rows.append(row_sum)
        cols.append(col_sum)
        row_sum, col_sum = 0, 0
    # find sum of diagonal 1
    for i in range(len(s)):
        diag_sum1 += s[i][i]
        diag_sum2 += s[len(s[0]) - i - 1][i]
    diags = [diag_sum1, diag_sum2]
    pass



# testing

s = [
    [1,4,3],
    [2,6,2],
    [3,2,7]
]
row_sum = 0
col_sum = 0
diag_sum1 = 0
diag_sum2 = 0


rows = []
cols = []
diags = []

for i in range(len(s)):
    for j in range(len(s)):
        row_sum += s[i][j]
        col_sum += s[j][i]
    rows.append(row_sum)
    cols.append(col_sum)
    row_sum, col_sum = 0, 0, 

for i in range(len(s)):
    diag_sum1 += s[i][i]
    diag_sum2 += s[len(s[0]) - i - 1][i]
diags = [diag_sum1, diag_sum2]



print(rows)
print(cols)
print(diags)
    