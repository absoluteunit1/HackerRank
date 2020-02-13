def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] >= 38:
            if (grades[i] + 2)%5 == 0:
                grades[i] += 2
            elif (grades[i] + 1)%5 == 0:
                grades[i] += 1
    return grades
    

a = [73,67,38,33]
print(gradingStudents(a))



