# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 02:10:11 2022

@author: Prashanth C S
"""

total_cost = 1000000

percent_down_payment = 0.25
portion_down_payment = percent_down_payment * total_cost
annual_return_rate = 0.04
annual_salary = 150000
monthly_salary = annual_salary/12
#portion_saved = int(input('Enter the percent of your salary to save: '))/100
#portion_saved_monthly = portion_saved * monthly_salary


annual_raise = 0.07
#enter_the_months = int(input("Enter the months you want to save for: "))
acceptable_difference = 100



def getTotalSavings(monthly_saving_rate, monthly_salary, annual_salary):
    monthly_saving_rate = monthly_saving_rate / 10000
    #print("monthly_saving_rate",monthly_saving_rate)
    
    current_savings = 0
    interest_accrued = 0
    #print("monthly_salary",monthly_salary)
    #print("annual_salary",annual_salary)
    portion_saved_monthly = monthly_saving_rate * monthly_salary
    #print("portion_saved_monthly",portion_saved_monthly)
    for i in range(1,37):
        monthly_interest = (current_savings*annual_return_rate)/12
        interest_accrued += monthly_interest
        current_savings += portion_saved_monthly + monthly_interest
        if(i % 6 == 0):
            annual_salary += annual_salary * annual_raise
            monthly_salary = annual_salary/12
            portion_saved_monthly = monthly_saving_rate * monthly_salary
    return round(current_savings)

count = 0

def getPercent(low, high):
    global count
    count += 1
    
    mid = (high + low) / 2
    #print("count:",count,"low, high, mid is ",low, high, mid)
    down_payment = round(portion_down_payment);
    savings = getTotalSavings(mid, monthly_salary, annual_salary)
    #print("savings: ",savings)
   # difference = savings - down_payment
    if count >= 12:
        return mid
    if( savings in range(down_payment-100, down_payment+100)):
        return mid
    if(savings < down_payment):
       return getPercent(mid, high)
    return getPercent(low, mid)



print(getPercent(0,10000)/10000)