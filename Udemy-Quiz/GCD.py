#Find the GCD of two numbers using recursion
# Implement the Euclidean Algorithm
# gcd(48,18):
#step 1 48//18 = 2 remainder 12
#step 2 18//12 = 1 remainder 6
#step 3 12//6 = 2 remainder 0

#gcd(a,0)=a
#gcd(a,b) = gcd(b, a%b)

def gcd(a,b):
	assert int(a) == a and int(b) == b , "The numbers must be integers only"
	#Convert negative numbers to positive numbers 
	if a < 0:
		a = -1 * a
	if b < 0:
		b = -1 * b
	if b == 0:
		return a
	else:
		return gcd(b, a%b)
a=48
b=18
print(gcd(a,b))
