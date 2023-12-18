#!/usr/bin/env python
# coding: utf-8

# # Unit of Measurement Converter
# 
# This is project 1 out of 5 in the Analyst Builder's Python Programing for Beginners Series. I will add my own changes and modifications compared to the one shown in the course.

# In[ ]:


print('\033[1m' + "===Converting Gasoline Prices for When You Cross the Border!===" + '\033[0m')
print("This can convert USD per Gallon to CAD per Liter and vice versa.")
print("Assumes 1 USD = 1.34 CAD as per Dec 18 2023")

convert_from = input("Would you like to convert from USD or CAD?: ")

# This statement makes sure that the user doesn't input a non-numeric value
while True:
    dollar_amount_input = input("Enter the amount you would like to be converted: ")
    try:
        dollar_amount = float(dollar_amount_input)
        break 
    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")

if convert_from.lower() in ["us", "usd", "us dollar", "american"]:
    print(dollar_amount, "USD per Gallon is approximately", round((dollar_amount * 1.34) / 3.78541, 2), "CAD per Liter")
elif convert_from.lower() in ["ca", "cad", "ca dollar", "canadian dollar", "canadian"]:
    print(dollar_amount, "CAD per Liter is approximately", round((dollar_amount / 1.34) * 3.78541, 2), "USD per Gallon")
else:
    print("This can only convert between USD and CAD and not other currencies! Please try again.")


# ### Project Overview and Lessons Learnt 
# 
# While this was relatively simple to create, it did teach me a lot about how to work with bugs in my code and how to fix the errors. 
# 
# I also learnt that the user may not input the currency in my desirded format so I accounted for that as well. 
# 
# I learnt how to use a WHILE LOOP for this project which shows the user that they have entered something other than an integer or float value for the dollar_amount. 
# 
# I would like to make this more user friendly and more interactive in the future if I come back to a project like this.

# In[ ]:




