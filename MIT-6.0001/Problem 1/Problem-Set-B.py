#Part B: Saving, with a raise
#Background 
#In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months. 
#In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify your program to include the following
#1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
#2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18  month, and so on. 
#Write a program to calculate how many months it will take you save up enough money for a down payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
#1. The starting annual salary (annual_salary)
#2. The percentage of salary to be saved (portion_saved)
#3. The cost of your dream home (total_cost)
#4. The semi­annual salary raise (semi_annual_raise)
#Hints
#To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
#● Retrieve user input. 
#● Initialize some state variables. You should decide what information you need. Be sure to be careful about values that represent annual amounts and those that represent monthly amounts.
#● Be careful about when you increase your salary – this should only happen after the 6th, 12th, 18th month, and so on. 
#Try different inputs and see how quickly or slowly you can save enough for a down payment.  
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter portion of your salary to be saved as a deciml of your percentage:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter your semi annual raise:"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

monthly_salary = annual_salary/12
months = 0

while current_savings < total_cost*portion_down_payment:
	#each month our current_savings increases by a factor of our monthly salary	
	current_savings += monthly_salary*portion_saved
	#Each month our current savings increases with a portion of our monthly salary and a portion of the current savings
	current_savings += current_savings*r/12
	if months % 6==0 and months > 0:
		#We want monthly salary to increase by a %  each 6 months		
		monthly_salary += monthly_salary*semi_annual_raise		
#		print("New monthly salary is:", monthly_salary)
	months += 1
	
print("Number of months to save for down payment:", months)
 
