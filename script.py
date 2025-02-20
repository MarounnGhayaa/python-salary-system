action = "yes"
salary_list = []
while action != "no":
    salary = float(input("Enter your salary: "))
    month = input("Enter the month you're storing the salary for: ")
    savings = float(input("Enter your savings percentage: "))
    rent = float(input("Enter your rent percentage: "))
    electricity = float(input("Enter your electricity percentage: "))
    allocated_savings = salary * savings / 100
    allocated_rent =  salary * rent / 100
    allocated_electricity = salary * electricity / 100
    calculations = {
        "salary": salary,
        "month": month,
        "savings": savings,
        "rent": rent,
        "electricity": electricity,
        "allocated_savings": allocated_savings,
        "allocated_rent": allocated_rent,
        "allocated_electricity": allocated_electricity,
    }
    salary_list.append(calculations)
    action = input("Do you want to proceed with another month (yes/no): ")
print(salary_list)
print("=" * 20)
print("Salaries summary!")
print("=" * 20)
for salary in salary_list:
    print(f"Month: {salary['month']}")
    print(f"Salary: {salary['salary']}$")
    print(f"Savings: {salary['savings']}% --> {salary['allocated_savings']}$")
    print(f"Rent: {salary['rent']}% --> {salary['allocated_rent']}$")
    print(f"Electricity: {salary['electricity']}% --> {salary['allocated_electricity']}$")
    print("=" * 40)
""" 
total_amount = allocated_savings + allocated_rent + allocated_electricity
print(f"Your total amount on allocations is: {total_amount}$.")
remainder = salary - total_amount
print(f"Your remainder is: {remainder}$.")
print(f"Your estimated yearly rent is {allocated_rent * 12}$, and your estimated yearly electricity costs are {allocated_electricity * 12}")
print(salary ** 2)
random_money = 50.0
print(f"If each month you had {random_money}$ for a year, {(random_money * 12) / (allocated_savings * 12)}$ will be left after diving by total amount allocated to savings.") """