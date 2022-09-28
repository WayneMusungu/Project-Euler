#Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. Recall that the Fibonacci sequence is the sequence of whole numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1, and where every number thereafter is equal to the sum of the previous two numbers.
#Examples

#1. fib(4) #3
#2. fib(10) #55
#3. fib(28) #317811
#4. fib(35) #9227465

def fib(num):
	if num < 2:
		return num
	else:
		#Use the Fibonacci formular f(n) = f(n-1) + f(n-2)
		return fib(num-1) + fib(num-2)
num = 10
print(fib(num))

