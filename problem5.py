"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""
count = 20
while count > 0:
    if count % 19 == 0 and count % 18 == 0 and count % 17 == 0 and count % 16 == 0 and count % 15 == 0 and count % 14 == 0 and count % 13 == 0 and count % 12 == 0 and count % 11 == 0:
        print(count)
        break
    else:
        count +=20