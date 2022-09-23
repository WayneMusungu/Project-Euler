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



