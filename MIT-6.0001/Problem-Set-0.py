#Assignment
# Write a program that does the following in order:
	#1. Asks the user to enter a number "x"
	#2. Asks the user to enter a number "y"
	#3. Prints out number "x" raised to the power "y"
	#4. Prints out the log(base2) of "x"

import math
def prog(base,exponent):
  if exponent == 0:
    return 1
  return base * prog(base, exponent-1)
base = int(input())
exponent = int(input())
logbase =round(math.log2(base),3)
print(prog(base,exponent))
print(logbase)
