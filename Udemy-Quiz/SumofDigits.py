#find the sum of digit
def sumofDigit(digit):
	total = 0
#1.Create a for loop and iterate over the stringified digit
#2.Convert each digit to an integer and add the sum
	for i in str(digit):
		total = total + int(i)
	return total
digit = 8976
print(sumofDigit(digit))

#Use recursive function
def sumofDigit(digit):
#Use assert keyword to find sum of positive integers numbers only
	assert digit >=0 and int(digit) == digit, "The number must be a positive integer only"
	if digit == 0:
		return 0
	else:
#Divide the digit with 10 and taking the remainder and sum it up with the next
#value of our next function f(digit)=digit%10+f(digit//10) which will be called recursively
#based on digit divided by 10
		return int(digit%10) + sumofDigit(digit//10)
print(sumofDigit(8976))


