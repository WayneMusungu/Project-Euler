"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
def is_prime(number):
  r = int(number**0.5)
  for x in range(2,r+1):
    if number % x == 0:
      return False
  return True

primelist = []
num = 1
while len(primelist) < 10001:
  num += 1
  if is_prime(num):
    primelist.append(num)
  
print(primelist[-1])