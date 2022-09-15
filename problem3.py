"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the
number 600851475143 ?
"""
n = 600851475143

def largestPrime(num):
    i = 2
    while i <= num:
        if num % i == 0:
            num = num/i
        else:
            i += 1
    return i

print(largestPrime(n))