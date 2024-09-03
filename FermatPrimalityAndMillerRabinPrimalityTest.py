import random

def repeatedSquareAndMultiply(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # If the exponent is odd
            result = (result * base) % modulus
        exponent = exponent >> 1  # Divide the exponent by 2
        base = (base * base) % modulus
    return result

def fermatPrimalityTest(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True

def millerRabinPrimalityTest(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    def checkComposite (d, n):
        a = random.randint(2, n - 2)
        x = repeatedSquareAndMultiply(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        if not checkComposite (d, n):
            return False
    return True

# Test the given numbers
numbers = [53982894593059, 88362852307, 12055296811267, 222334565193641]

fermat_results = {num: fermatPrimalityTest(num, 10) for num in numbers}
miller_rabin_results = {num: millerRabinPrimalityTest(num, 10) for num in numbers}

print("Fermat Primality Test Results:")
for num, result in fermat_results.items():
    print(f"{num}: {'Prime' if result else 'Composite'}")

print("\nMiller-Rabin Primality Test Results:")
for num, result in miller_rabin_results.items():
    print(f"{num}: {'Prime' if result else 'Composite'}")