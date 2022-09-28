#Factorial
#Write a function factorial which accepts a number and returns the factorial of that number. A factorial is the product of an integer and all the integers below it; e.g., factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24,factorial zero (0!) is always 1.

#Examples
#1. factorial(1) # 1
#2. factorial(2) # 2
#3. factorial(4) # 24
#4. factorial(7) # 5040#

#Using iterative apprroach

def factorial(num):
	total = 1
	for i in range(1, num+1):
		total *= i
	return total

num = 3 
print(factorial(num))

#Using recursive approach

def factorial(num):
	if num == 0:
		return 1
	else:
		return(num * factorial(num-1))
num = 4 
print(factorial(num))
