# My Solution
# doesn't work for large test cases

def acmTeam2(topic):
    
    numbeOfWays = 0
    highestSum = 0
    wordLength = len(topic[0])

    sums = []

    for i in range(len(topic) - 1):
        for j in range(i + 1,len(topic)):

            a = [int(x) for x in topic[i]]
            b = [int(x) for x in topic[j]]
            added = sum ( a[x] or b[x] for x in range(wordLength) )
            if added > highestSum:
                highestSum = added
            sums.append(added)

    numbeOfWays = sums.count(highestSum)
    return [highestSum, numbeOfWays]

# Another Solution

# This is a solution that passes all the tests.
#   My mistake in previous solutions was that I was assuming the max number of topics a person can know is the 
# length of the topics list (meaning that all the elements of the string are 1) and so I used len(topic[0]).
# The correct answer is to return the max number 2 people can based on the input (the total number of 1s in a combined string that has the max # of 1s)

def acmTeam3(topic):

    # Add up all the ones in from two lists and return their
    # zip() function returns a zip object, which is an iterator of tuples where the the first item in 
    # each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    def add(p1, p2):
        return sum((i or j) for i, j in zip(p1, p2))

    persons = []

    # turns each string into a list of int 1s and 0s. And appends those lists to persons list
    for i in range(len(topic)):
        persons.append([int(topic[i][x]) for x in range(len(topic[i]))])
    
    total = []

    # exclude the last one (len(persons) - 1) because at the end of the list we will compare the second last item with the last item (avoid comparing the last item with itself)
    # we add all the 1s from both lists (remember: (i or j) from add function, it adds the higher value of i or j ) and append it to the total 
    # total is a list of all the total 1s added for each combination of lists 
    for i in range(len(persons) - 1):
        for j in range(i + 1,len(persons)):
            total.append(add(persons[i], persons[j]))

    # highest returns the maximum number from totals (highest number of 1s in a combined list) "...the maximum number of topics a 2-person team can know"
    highest = max(total)
    # total.count(highest) returns a number of how many times the highest number occurs in the list total.
    return [highest, total.count(highest)]