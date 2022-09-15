"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product
of two 3-digit numbers.
"""
x = range(1, 999)
l = []

for y in x:
    for z in x:
        a = y * z
        if str(a) == str(a)[::-1]:
            l.append(a)
            
print(max(l))