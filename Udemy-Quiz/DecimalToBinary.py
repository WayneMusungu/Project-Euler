def decimalToBinary(num):
	if (num==0):
		return
	else:
		decimalToBinary(int(num/2))
		print(num%2, end="")
decimalToBinary(10)
