def isPrime(number):
    for elem in range(2, number // 2 + 1):
        if number % elem == 0:
            return False
    return True