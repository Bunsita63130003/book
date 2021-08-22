First_number = float(input("Enter the first number :"))
Second_number = float(input("Enter the Second number :"))
Operator = input("Enter the operator :")

if (Operator == '+'):
    print("the answer is", round((First_number + Second_number), 2))
elif(Operator == '-'):
    print("the answer is", round((First_number - Second_number), 2))
elif(Operator == '*'):
    print("the answer is", round((First_number * Second_number), 2))
elif(Operator == '/'):
    print("the answer is", round((First_number / Second_number), 2))
elif(Operator == '%'):
    print("the answer is", round((First_number % Second_number), 2))
else:
    print("ERROR!!!")