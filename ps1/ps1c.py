# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:57:54 2022

@author: Prashanth C S
"""
total_cost = int(input('Enter the cost of your dream home: '))
current_savings = 0
percent_down_payment = int(input("Enter the percent of downpayment you wish to make: "))/100
portion_down_payment = percent_down_payment * total_cost
annual_return_rate = int(input("Enter expected annual return rate: "))/100
annual_salary = int(input('Enter your annual salary: '))
monthly_salary = annual_salary/12
#portion_saved = int(input('Enter the percent of your salary to save: '))/100
#portion_saved_monthly = portion_saved * monthly_salary

interest_accrued = 0
annual_raise = int(input("Enter the expected annual raise, as percent: "))/100
target_months = int(input("Enter the months you want to save for: "))
acceptable_difference = 100





def getTotalSavings(monthly_saving_rate, monthly_salary, annual_salary):
    #print("\n\n\n")
    monthly_saving_rate = monthly_saving_rate / 10000
    #print("monthly_saving_rate",monthly_saving_rate)
    
    current_savings = 0
    interest_accrued = 0
    portion_saved_monthly = monthly_saving_rate * monthly_salary
    for i in range(1,target_months):
        monthly_interest = (current_savings*annual_return_rate)/12
        interest_accrued += monthly_interest
        current_savings += portion_saved_monthly + monthly_interest
        if(i % 12 == 0):
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
    if( savings in range(down_payment-acceptable_difference, down_payment+acceptable_difference)):
        return mid
    if(savings < down_payment):
       return getPercent(mid, high)
    return getPercent(low, mid)

result = round(getPercent(0,10000)/10000,4)*100

print("\n\n"+50*"*"+"\nOptimal saving rate:",result,"%\n"+50*"*")
    
   
    
    

