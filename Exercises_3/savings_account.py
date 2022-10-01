interest_rate = float(input("Enter interest rate: "))
income_tax_rate = float(input("Enter capital income tax rate: "))
initial_deposit = int(input("Enter initial deposit: "))
years = int(input("Enter number of years: "))
print("")

balance = initial_deposit
for i in range(1, (years)+1):
    interest = balance * interest_rate / 100
    income_tax = interest * income_tax_rate / 100
    new_balance = interest - income_tax
    balance += new_balance
    print(f"Year {i}: {balance:.2f}")
