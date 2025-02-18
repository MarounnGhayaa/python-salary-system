salary = float(input("Enter your salary: "))
month = input("Enter the month you're storing the salary for: ")
savings = int(input("Enter your savings percentage: "))
rent = int(input("Enter your rent percentage: "))
electricity = int(input("Enter your electricity percentage: "))
allocated_savings = salary * savings / 100
allocated_rent =  salary * rent / 100
allocated_electricity = salary * electricity / 100
print(f"Your salary {salary}$") 
print(f"Your savings percentage {savings}%, your allocated savings amount will be {allocated_savings}$")
print(f"Your rent percentage {rent}%, your allocated rent amount will be {allocated_rent}$")
print(f"Your electricity percentage {electricity}%, your allocated electricity amount will be {allocated_electricity}$.")
total_amount = allocated_savings + allocated_rent + allocated_electricity
print(f"Your total amount on allocations is: {total_amount}$.")
remainder = salary - total_amount
print(f"Your remainder is: {remainder}$.")
print(f"Your estimated yearly rent is {allocated_rent * 12}$, and your estimated yearly electricity costs are {allocated_electricity * 12}")
print(salary ** 2)