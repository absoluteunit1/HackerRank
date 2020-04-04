from copy import copy, deepcopy

# a function for matrix transposition. 
# I noticed a pattern that if the sums of columns and sum of rows have the same amount of odd sums, then the swapping will be possible 
# Alas, it only passed the 4/7 test cases. There are certain edge cases that prevent this.

def organizeContainers2(container):
    def transpose(matrix):
        transposed_matrix = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                    transposed_matrix[j][i] = matrix[i][j]
        return transposed_matrix
    
    transposed_container = transpose(container)
    odd = 0
    t_odd = 0

    for row in range(len(container)):
        if (sum(container[row]))%2 == 1:
            odd += 1
        if (sum(transposed_container[row]))%2 == 1:
            t_odd += 1
    return "Possible" if t_odd == odd else "Impossible"
    



container = [   [0,2,1],
                [1,1,1],
                [2,0,0]
]

container2 = [   [1,1],
                 [1,1]
]

container3 = [
                [999336263, 998799923],
                [998799923, 999763019]

]

container4 = [
                [997612619, 934920795, 998879231, 999926463],
                [960369681, 997828120, 999792735, 979622676],
                [999013654, 998634077, 997988323, 958769423],
                [997409523, 999301350, 940952923, 993020546]
]
print(organizeContainers2(container2))
print(organizeContainers2(container))
print(organizeContainers2(container4))
