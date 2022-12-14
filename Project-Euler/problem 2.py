"""
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting
with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not eaceed four million,
find the sum of the even-valued terms.
"""

a = 0
b = 1
sum = 0

while b < 4000000:
    a=a+b
    b=a+b
    if a%2 == 0:
        sum = sum + a
    if b%2 == 0:
        sum = sum + b 

print(f"The sum of the even valued term is {sum}")