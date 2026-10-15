# def average(num1, num2,num3):
#     total = num1 + num2 +num3
#     return total / 3
#
#
# print(average(11,21,31))
# print(average(40,40,40))


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(10))


def factorial(n):
    result =1

    for i in range(1,n+1):
        result *= i

    return result

print(factorial(5))