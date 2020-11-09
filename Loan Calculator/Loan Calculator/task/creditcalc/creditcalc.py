import math
import argparse

# Phase 1
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
loan_principal = 0
print(loan_principal, first_month, second_month, third_month, final_output, sep='\n')

# Phase 2
loan_principal = 0
def monthly_payment_calc():
    months_to_repay = int(input('Enter the number of months: \n'))
    monthly_payment = math.ceil(loan_principal / months_to_repay)
    if loan_principal % months_to_repay != 0:
        last_payment = loan_principal - ((months_to_repay - 1) * monthly_payment)
        print(f'Your monthly payment = {monthly_payment} and the last payment = {last_payment}')
    else:
        print(f'Your monthly payment = {monthly_payment}')


def number_of_monthly_payments_calc():
    monthly_payment = int(input('Enter the monthly payment: \n'))
    months_to_repay = math.ceil(loan_principal / monthly_payment)
    month_count = 'month' if months_to_repay == 1 else 'months'
    print(f'It will take {months_to_repay} {month_count} to repay the loan')


def calc_choice():
    global loan_principal
    loan_principal = int(input('Enter the loan principal: \n'))
    calculation_choice = input('What do you want to calculate? \n'
                               'type "m" - for the number of monthly payments, \n'
                               'type "p" - for the monthly payment: \n')
    if calculation_choice == 'm':
        number_of_monthly_payments_calc()
    if calculation_choice == 'p':
        monthly_payment_calc()

calc_choice()

# Phase 3
def annuity_calc_choice():
    calculation_choice = input('What do you want to calculate? \n'
                               'type "n" for the number of monthly payments, \n'
                               'type "a" for annuity monthly payment amount, \n'
                               'type "p" for loan principal, \n')
    if calculation_choice == 'n':
        calc_number_of_payments()
    if calculation_choice == 'a':
        calc_monthly_payment()
    if calculation_choice == 'p':
        calc_loan_principal()


def calc_number_of_payments():
    loan_principal = int(input('Enter the loan principal: \n'))
    monthly_payment = float(input('Enter the monthly payment: \n'))
    loan_interest = float(input('Enter the loan interest: \n'))/100
    nominal_interest = loan_interest / 12
    logbase = 1 + nominal_interest
    log = monthly_payment / (monthly_payment - nominal_interest * loan_principal)
    number_of_payments = math.ceil(math.log(log, logbase))
    number_of_payments_years = number_of_payments // 12
    year_count = 'year' if number_of_payments_years == 1 else 'years'
    number_of_payments_months = number_of_payments % 12
    month_count = 'month' if number_of_payments_months == 1 else 'months'
    if number_of_payments_years == 0:
        print(f'It will take {number_of_payments_months} {month_count} to repay this loan!')
    elif number_of_payments_months == 0:
        print(f'It will take {number_of_payments_years} {year_count} to repay this loan!')
    else:
        print(f'It will take {number_of_payments_years} {year_count} and {number_of_payments_months} {month_count} to repay this loan!')


def calc_monthly_payment():
    loan_principal = int(input('Enter the loan principal: \n'))
    number_of_payments = int(input('Enter the number of periods: \n'))
    loan_interest = float(input('Enter the loan interest: \n'))/100
    nominal_interest = loan_interest / 12
    numerator = nominal_interest * pow((1 + nominal_interest), number_of_payments)
    denominator = pow((1 + nominal_interest), number_of_payments) - 1
    monthly_payment = math.ceil(loan_principal * (numerator/denominator))
    print(f'Your monthly payment = {monthly_payment}!')


def calc_loan_principal():
    monthly_payment = float(input('Enter the monthly payment: \n'))
    number_of_payments = int(input('Enter the number of periods: \n'))
    loan_interest = float(input('Enter the loan interest: \n'))/100
    nominal_interest = loan_interest / 12
    numerator = nominal_interest * pow((1 + nominal_interest), number_of_payments)
    denominator = pow((1 + nominal_interest), number_of_payments) - 1
    loan_principal = monthly_payment / (numerator/denominator)
    print(f'Your loan principal = {loan_principal}!')


annuity_calc_choice()


# Phase 4

def initialize_cli_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--type', choices=['annuity', 'diff'], help='input type of payment: annuity or diff')
    parser.add_argument('--interest', type=float, help='input interest as a whole number without the percent symbol')
    parser.add_argument('--payment', type=float, help='input monthly payment amount for annuity; not valid for diff')
    parser.add_argument('--principal', type=float, help='total loan balance')
    parser.add_argument('--periods', type=float, help='months needed to repay the loan')

    return parser


def check_cli_input(user_input, p, n, i, pmt):
    if user_input is None or i is None:
        print('Incorrect parameters')
    else:
        i = i / 100 / 12
        if user_input == 'annuity':
            # check if monthly pmt calc
            if pmt is None:
                if n is None or p is None:
                    print('Invalid input - missing input for pmt calc')
                else:
                    calc_annuity_pmt(n, p, i)
            # check number of pmts calc
            elif n is None:
                if p is None or pmt is None:
                    print('Invalid input - missing input for n calc')
                else:
                    calc_annuity_n(p, pmt, i)
            # check if principal calc
            elif p is None:
                if pmt is None or n is None:
                    print('Invalid input - missing input for prin calc')
                else:
                    calc_annuity_principal(pmt, n, i)
        elif user_input == 'diff':
            if p is None or n is None:
                print('Invalid input - missing input for diff calc')
            else:
                calc_diff(p, n, i)


def calc_diff(p, n, i):
    m = 1
    total_payment = 0
    while True:
        payment = math.ceil((p/n) + (i * (p - ((p * (m - 1)) / n))))
        print(f'Month {m}: payment is {payment}')
        m += 1
        total_payment += payment
        if total_payment > p:
            overpayment = total_payment - p
            print(f'\nOverpayment = {overpayment}')
            break


def calc_annuity_n(p, pmt, i):
    logbase = 1 + i
    log = pmt / (pmt - i * p)
    number_of_payments = math.ceil(math.log(log, logbase))
    number_of_payments_years = number_of_payments // 12
    year_count = 'year' if number_of_payments_years == 1 else 'years'
    number_of_payments_months = number_of_payments % 12
    month_count = 'month' if number_of_payments_months == 1 else 'months'
    if number_of_payments_years == 0:
        print(f'It will take {number_of_payments_months} {month_count} to repay this loan!')
    elif number_of_payments_months == 0:
        print(f'It will take {number_of_payments_years} {year_count} to repay this loan!')
    else:
        print(f'It will take {number_of_payments_years} {year_count}'
              f'and {number_of_payments_months} {month_count} to repay this loan!')
    total_pmt = number_of_payments * pmt
    if total_pmt > p:
        overpayment = total_pmt - p
        print(f'Overpayment = {overpayment}')


def calc_annuity_principal(pmt, n, i):
    numerator = i * pow((1 + i), n)
    denominator = pow((1 + i), n) - 1
    p = math.floor(pmt / (numerator/denominator))
    print(f'Your loan principal = {p}!')

    total_pmt = n * pmt
    if total_pmt > p:
        overpayment = total_pmt - p
        print(f'Overpayment = {overpayment}')


def calc_annuity_pmt(n, p, i):
    numerator = i * pow((1 + i), n)
    denominator = pow((1 + i), n) - 1
    pmt = math.ceil(p * (numerator/denominator))
    print(f'Your monthly payment = {pmt}!')
    total_pmt = n * pmt
    if total_pmt > p:
        overpayment = total_pmt - p
        print(f'Overpayment = {overpayment}')


def main():
    argument_parsing_configuration = initialize_cli_arguments()
    args = argument_parsing_configuration.parse_args()
    # print(args)

    user_input = args.type
    p = args.principal
    n = args.periods
    i = args.interest
    pmt = args.payment

    check_cli_input(user_input, p, n, i, pmt)


main()
