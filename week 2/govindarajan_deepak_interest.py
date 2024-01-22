def interest():
    loan_principal=int(input("Please enter the loan principal in dollars: "))
    loan_term=int(input("Please enter the loan term in months: "))
    loan_interest=float(input("Please enter the annual interest rate on the loan in decimal: "))
    interest_amount=(loan_principal*(1+(loan_interest/12))**loan_term)-loan_principal
    print(f'The interest amount is ${interest_amount}.')

interest()
