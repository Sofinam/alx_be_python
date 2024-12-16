monthly_income = float (input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculating monthly savings
monthly_savings = monthly_expenses - monthly_income

#Projecting annual savings
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are: ${monthly_savings:}")
print("Your projected savings after one year is: ${projected_savings:}")
