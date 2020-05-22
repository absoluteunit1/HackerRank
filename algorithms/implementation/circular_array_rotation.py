

def solution(a, k):
    a = a[len(a)-k%len(a):] + a[:len(a)-k%len(a)]
    return a
    

print(solution([1,2,3,4,5,6,7], 16 ))