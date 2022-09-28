#Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

#Examples
# 1. recursiveRange(6) # 21
# 2. recursiveRange(10) # 55

def recursiveRange(num):
	if num <= 0:
		return 0
	else:
		return num + recursiveRange(num-1)
num = 10
print(recursiveRange(num))

# Use iterative Approach
def iterativeRange(num):
	total = 0
	for i in range(1,num+1):
		total += i
	return total
num = 6
print(iterativeRange(num))
