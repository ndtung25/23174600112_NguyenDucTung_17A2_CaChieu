def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    twin_primes = []
    for i in range(3, limit, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

limit = 1000
twin_primes = find_twin_primes(limit)

for twin in twin_primes:
    print(twin)
