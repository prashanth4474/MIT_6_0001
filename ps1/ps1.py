# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:01:22 2022

@author: Prashanth C S
"""

total_cost = int(input('Enter the cost of your dream home: '))
current_savings = 0
percent_down_payment = int(input("Enter the percent of downpayment you wish to make: "))/100
portion_down_payment = percent_down_payment * total_cost
annual_return_rate = int(input("Enter expected annual return rate: "))/100
annual_salary = int(input('Enter your annual salary: '))
monthly_salary = annual_salary/12
portion_saved = int(input('Enter the percent of your salary to save: '))/100
portion_saved_monthly = portion_saved * monthly_salary
months = 0
interest_accrued = 0
annual_raise = int(input("Enter the expected annual raise, as percent: "))/100


while(current_savings < portion_down_payment):
    monthly_interest = (current_savings*annual_return_rate)/12
    interest_accrued += monthly_interest
    current_savings += portion_saved_monthly + monthly_interest
    months += 1
    if(months % 12 == 0):
        annual_salary += annual_salary * annual_raise
        monthly_salary = annual_salary/12
        portion_saved_monthly = portion_saved * monthly_salary

print("Number of months to save the downpayment:",months)
print("Your saving after",months,"months: ", round(current_savings))
print("Interest accrued: ",round(interest_accrued))
print("Capital invested: ",round(portion_saved_monthly*months))
print("Your annual salary at the time of downpayment: ", annual_salary, " monthly salary: ",annual_salary/12)
    

