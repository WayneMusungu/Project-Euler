#Write a program to find all pairs of integers whose sum is equal to a given number
#[2,6,3,9,11] 9 -> [6,3]


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]

#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

#Write a program to find all pairs of integers whose sum is equal to a given number.
#[2,6,3,9,11] 9 -> [6,3]



#- Does array contain only positive or negative numbers?
#- What if the same pair repeats twice, should we print it every time?
#- If the reverse of the pair is acceptable e.g. can we print both (4,1) and (1,4) if the given sum is 5.
#- Do we need to print only distinct pairs? does (3, 3) is a valid pair forgiven sum of 6?
#- How big is the array?

def findPairs(nums, target):
  for i in range(len(nums)):
    for j in range (i+1, len(nums)):
      if nums[i] == nums[j]:
        continue
      elif nums[i] + nums[j] == target:
        print([i,j])
mylist = [2,7,11,15]
findPairs(mylist,9)








                    
