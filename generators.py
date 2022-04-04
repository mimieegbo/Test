def primes_():
    yield 2
    yield 3

    number = 3
    primes = [2, 3]

    while True:
        isNotPrime = False
        for p in primes:
            if number % p == 0:
                isNotPrime = True
                break
        if isNotPrime:
            number += 2
            continue
        primes.append(number)
        yield number
        number += 2


# count = 0
# for p in primes_():
#     print(p)
#     if count == 1000:
#         break
#     count += 1

# for i in range(10):
#     print(next(primes_()))

small = [1, 3, 5, 6, 5, 6, 7]

small = iter(small)

for i in range(3):
    print(next(small))
print(next(small))
print(next(small))
print(next(small))
print(next(small))


