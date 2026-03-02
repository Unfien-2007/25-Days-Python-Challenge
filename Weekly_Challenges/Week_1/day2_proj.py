#salary calculator for the role
monthly_salary: float = float(input("Enter Monthly Salary: "))
Yearly_salary: float = monthly_salary * 12
_13month_salary: float = Yearly_salary / 12

print("=" * 60)
print("Monthly Salary Calculator")
print("=" * 60)
print(f"With PHP {monthly_salary:.2f} Monthly Salary")
print(f"You would have PHP {Yearly_salary:.2f} Yearly Salary")
print(f"and a total salary of PHP {Yearly_salary + _13month_salary:.2f} before tax.")
