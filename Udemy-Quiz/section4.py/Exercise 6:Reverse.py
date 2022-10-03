#Write a recursive function called reverse which accepts a string and returns a new string in reverse.

#Examples

#reverse('python') # 'nohtyp'
#reverse('appmillers') # 'srellimppa'

#Use Recursive function
def reverse(strng):
    if len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
strng="appmillers"
print (reverse(strng))


#Using an extended slice
def reverse(strng):
	return strng[::-1]
strng="python"
print(reverse(strng))


