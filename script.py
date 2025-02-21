def allocations(salary, amount):
    allocation = salary * amount /100
    return allocation

def totalSum(spending1, spending2, spending3):   
    total = spending1 + spending2 + spending3
    return total

action = "yes"
salary_list = []
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
while action != "no":
    salary = float(input("Enter your salary: "))
    while True:
        month = input("Enter the month you're storing the salary for: ").lower()
        if month not in months:
            print("Invalid month! Make sure to input an actual month.")
            continue
        duplicate = False
        for salary_month in salary_list:
            if salary_month['month'] == month:
                duplicate = True
                break
        if duplicate:
            print(f"{salary_month['month']} has already been added.")
            continue
        break
    while True:
        savings = float(input("Enter your savings percentage: "))
        rent = float(input("Enter your rent percentage: "))
        electricity = float(input("Enter your electricity percentage: "))
        if savings < 0 or savings > 100 or rent < 0 or rent > 100 or electricity < 0 or electricity > 100:
            print("Each percentage must be between 0 and 100.")
            continue
        if savings + rent + electricity > 100:
            print("The total of percentages exceeds 100.")
            continue
        break
    allocated_savings = allocations(salary, savings)
    allocated_rent =  allocations(salary, rent)
    allocated_electricity = allocations(salary, electricity)
    random_money = float(input("Enter extra amount of money as an income if any: "))
    calculations = {
        "salary": salary,
        "month": month,
        "savings": savings,
        "rent": rent,
        "electricity": electricity,
        "allocated_savings": allocated_savings,
        "allocated_rent": allocated_rent,
        "allocated_electricity": allocated_electricity,
        "random_money": random_money,
    }
    salary_list.append(calculations)
    action = input("Do you want to proceed with another month (yes/no): ").lower()
print("=" * 20)
print("Salaries summary!")
print("=" * 20)
for salary in salary_list:
    print(f"Month: {salary['month']}")
    print(f"Salary: {salary['salary']}$ / Extra money: {salary['random_money']}$")
    print(f"Savings: {salary['savings']}%       -->       {salary['allocated_savings']}$")
    print(f"Rent: {salary['rent']}%          -->       {salary['allocated_rent']}$")
    print(f"Electricity: {salary['electricity']}%   -->       {salary['allocated_electricity']}$")
    print(f"(Salary^2 --> {salary['salary'] ** 2}$)")
    print(f"Total amount spent on savings, rent and electricity is: {totalSum(allocated_savings, allocated_rent, allocated_electricity)}$")
    print(f"The remainder of the salary including savings is: { salary['salary'] - (salary['allocated_rent'] + salary['allocated_electricity'])}$")
    print(f"(Excluding savings --> { salary['salary'] - (salary['allocated_rent'] + salary['allocated_electricity'] + salary['allocated_savings'])}$)")
    print("According to this month:")
    print(f"- Your estimated yearly electricity is: {salary['allocated_electricity'] * 12}$")
    print(f"- Your estimated yearly rent is: {salary['allocated_rent'] * 12}$")
    if salary['random_money'] == 0:
        print("No extra money gained!")
    elif salary['allocated_savings'] == 0:
        print(f"- If each month you had {salary['random_money']}$ for a year: \n {salary['random_money'] * 12}$ will be left to you. (No total amount allocated to savings to divide by!)")
    else:
        print(f"- If each month you had {salary['random_money']}$ for a year: \n {(salary['random_money']) / (salary['allocated_savings'])}$ will be left after diving by total amount allocated to savings.")
    print("=" * 85)