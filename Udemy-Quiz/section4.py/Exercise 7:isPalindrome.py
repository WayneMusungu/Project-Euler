#Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.
#Examples
# 1. isPalindrome('awesome') # false
# 2. isPalindrome('foobar') # false
# 3. isPalindrome('tacocat') # true
# 4. isPalindrome('amanaplanacanalpanama') # true
# 5. isPalindrome('amanaplanacanalpandemonium') # false


def isPalindrome(strng):
    if len(strng) < 1:
        return True
    else:
        if strng[0] == strng[-1]:
	#If the last letter is equal to the first letter, the function is called recursively with the argument as the sliced list with the first character and last character removed, else return False.
            return isPalindrome(strng[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(isPalindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")


def isPalindrome(strng):
    if strng == strng[::-1]:
        return True
    else:
        return False

strng="amanaplanacanalpanama"
print(isPalindrome(strng))

