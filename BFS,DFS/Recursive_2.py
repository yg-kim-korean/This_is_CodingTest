def factorial_iterative(n): #반복으로 구현
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n): #재귀로 구현
    if n<= 1 :
        return 1
    return n * factorial_recursive(n-1)

print('반복으로 구현',factorial_iterative(5))
print('재귀로   구현',factorial_recursive(5))