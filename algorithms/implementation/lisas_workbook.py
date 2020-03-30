# n = chapters
# arr[i] contains the # of problems numbered 1 - arr[i]
# each page can have up to k problems
# only last page can have less than k problems 

# My solution (passed all test cases)

def workbook(n, k, arr):
    pages = [None]

    for chapter in range(n):
        problem_set = []
        counter = 1
        for i in range(arr[chapter]):
            problem_number = i + 1
            if counter <= k:
                problem_set.append(problem_number)
                counter += 1
            else:
                pages.append(problem_set)
                problem_set = []
                problem_set.append(problem_number)
                counter = 2
        pages.append(problem_set)

    result = 0

    for i in range(1,len(pages)):
        for j in range(len(pages[i])):
            if i == pages[i][j]:
                result += 1

    return result


                
            




