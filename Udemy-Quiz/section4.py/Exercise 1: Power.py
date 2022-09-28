#POWER
#Write a function called power which accepts a base and an exponent. The function should return the power of the base to the exponent. This function should mimic the functionality of math.pow() - do not worry about negative bases and exponents.

#Examples
# 1.power(2,0)
# 2.power(2,2)
# 3.power(2,4)

def power(base,exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	return base * power(base, exponent-1)
base = 2
exponent = 4
print(power(base,exponent))

