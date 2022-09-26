#Calculate power of a number using recursion
def power(base, exponent):
#We use the formula x^n= x * x^n-1
	assert exponent >=0 and int(exponent)== exponent, "The exponent must be a positive integer only"
	if exponent == 0:
		return 1
	if exponent == 1:
		return base	
	return base * power(base, exponent-1)
print(power(7,2))

#Calculate power of a number using iteration
def power(base, exponent):
	result = 0
	for i in range(exponent):
		result *= base
	return result
print(pow(7,4))
 
