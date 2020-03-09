# Method One
# Bubble Sort

def bubble_sort(grades):
        for i in range(len(grades)-1):
                for j in range(0, len(grades) -1 -i):
                        if grades[j][1] > grades[j+1][1]:
                                grades[j], grades[j+1]  = grades[j+1], grades[j]
        return grades


# Method Two
# Using sort function

def sortGrades(grades):
        grades.sort(key = lambda x: x[1])
        return grades

# Method Three
# Using sorted()

def sortedGrades(grades):
        return sorted(grades, key = lambda x: x[1])

# SOLUTION

grades = []

for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])

def bubble_sort(grades):
        for i in range(len(grades)-1):
                for j in range(0, len(grades) -1 -i):
                        if grades[j][1] > grades[j+1][1]:
                                grades[j], grades[j+1]  = grades[j+1], grades[j]
        return grades

bubble_sort(grades)

secondLowest = (sorted({grades[i][1] for i in range(len(grades))}))[1]

students = []

for i in range(len(grades)):
        if grades[i][1] == secondLowest:
                students.append(grades[i][0])

students.sort()
for i in students:
        print(i)
