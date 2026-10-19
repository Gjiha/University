import random as rm


def trivialTest(n):
    if n==2 or n==3:
        return True
    if (n % 2) == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if (n % i) == 0:
            return False
    return True

def fermatTest(n, t=10):
    for _ in range(t):
        a = rm.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True


# error = 0
# listOfErrors = []
# for n in range(4, 10**6):
#     if fermatTest(n) != fermatTest(n):
#         error += 1
#         listOfErrors.append(n)

# print(listOfErrors)
# print("ERR ", error)
# print(error, (error / n)*100, '%')

def getPrime(b):
    flag = False
    while not flag:
        n = rm.randint(2**(b-1), 2**b - 1)
        flag = fermatTest(n)
    return n

x = getPrime(64)

print(trivialTest(x))