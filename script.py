action = "yes"
salary_list = []
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
random_money = 50.0
while action != "no":
    salary = float(input("Enter your salary: "))
    month = input("Enter the month you're storing the salary for: ").lower()
    while month not in months:
        month = input("Enter the month you're storing the salary for: ").lower()
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
    action = input("Do you want to proceed with another month (yes/no): ").lower()
print("=" * 20)
print("Salaries summary!")
print("=" * 20)
for salary in salary_list:
    print(f"Month: {salary['month']}")
    print(f"Salary: {salary['salary']}$ - [salary^2 = {salary['salary'] ** 2}]")
    print(f"Savings: {salary['savings']}%       -->       {salary['allocated_savings']}$")
    print(f"Rent: {salary['rent']}%          -->       {salary['allocated_rent']}$")
    print(f"Electricity: {salary['electricity']}%   -->       {salary['allocated_electricity']}$")
    print(f"Total amount spent on savings, rent and electricity is: {salary['allocated_savings'] + salary['allocated_rent'] + salary['allocated_electricity']}$")
    print(f"The remainder of the salary including savings is: { salary['salary'] - (salary['allocated_rent'] + salary['allocated_electricity'])}$")
    print("According to this month:")
    print(f"- Your estimated yearly electricity is: {salary['allocated_electricity'] * 12}$")
    print(f"- Your estimated yearly rent is: {salary['allocated_rent'] * 12}$")
    if salary['allocated_savings'] == 0:
        print(f"- If each month you had {random_money}$ for a year: \n {random_money * 12}$ will be left after diving by total amount allocated to savings.")
    else:
        print(f"- If each month you had {random_money}$ for a year: \n {(random_money * 12) / (salary['allocated_savings'] * 12)}$ will be left after diving by total amount allocated to savings.")
    print("=" * 70)