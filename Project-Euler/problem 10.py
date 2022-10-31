"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
primes=[2]
for i in range(3,2000001,2):
    prime = True
    for prime in primes:
        if prime > i**0.5:
            break
        if i%prime==0:
            prime=False
            break
    if prime:
        primes.append(i)
sum = 0
for prime in primes:
    sum += prime

print(sum)
