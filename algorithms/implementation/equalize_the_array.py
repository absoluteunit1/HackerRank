# My solution 
def equalizeArray(arr):
    counts = {i : arr.count(i) for i in arr}
    a = max(counts, key=counts.get)
    return len(arr) - len([i for i in arr if i == a]) 

# Another solution


def equalizeArray2(arr):
    return len(arr) - max([arr.count(t) for t in set(arr)])     # arr.count(t) for t in set(arr) returns a list that contains the counts of each number. The difference between the length of original list and the max occurence of a number, is how many deletions need to be done
    
