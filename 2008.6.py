# Significant constants
Tax_rate = 0.20
Standard_deduction = 10000.0
Dependent_deduction = 3000.0

# Input are
grossIncome = float(input("Enter the gross income : "))
numDependent = int(input("Enter the number of dependents:"))

# Computations
taxableIncome = grossIncome - Standard_deduction - Dependent_deduction * numDependent
incomeTax = taxableIncome * Tax_rate

# The outputs are
print("The income tax is $" + str(round(incomeTax, 2)))
