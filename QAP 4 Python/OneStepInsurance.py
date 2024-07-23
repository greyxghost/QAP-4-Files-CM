# Description: A Program for One Stop Insurance Company to enter and calculate new insurance policy information for its clients.
# Author: Chris M!
# Date(s): July 18 - 22, 2024

# Define required libraries:
import datetime
import time
import sys
import FormatLibrary as FL

# Define program constants:
f = open("Const.dat")

# The following line reads the first record
constants = f.readlines()

# Values from the list assigned to variables.
POLICY_NUM = int(constants[0].strip())
INSURANCE_PREM_BASE = float(constants[1].strip())
ADD_VEHC_DISCOUNT_RATE = float(constants[2].strip())
CAR_LIABILITY_RATE = float(constants[3].strip())
GLASS_COVER_RATE = float(constants[4].strip())
LOAN_CAR_RATE = float(constants[5].strip())
HST_RATE = float(constants[6].strip())
PROCESSING_FEE = float(constants[7].strip())

CAN_PROV = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
PAYMENT_TYPE = ["Full", "Monthly", "Down Payment"]
CURR_DATE = datetime.datetime.now()

# ADD 3 FUNCTIONS TO THE PROGRAM
# Define program functions:
def first_payment_date ():
    invoiceDate = CURR_DATE
    nextMonthPay = invoiceDate.month % 12 + 1
    nextYearPay = invoiceDate.year + (invoiceDate.month // 12)
    firstPaymentDate = datetime.date(nextYearPay, nextMonthPay, 1)
    return firstPaymentDate

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def address_formatting():
    return f"{custAdd}\n{" " * 19}{custCity}, {custProv}\n{" " * 19}{custPostCode}"

# ANSI escape codes for bold text (ANSI escape sequences are a standard for in-band signaling to control cursor location, color, font styling, and other options)
BOLD = '\033[1m'
END = '\033[0m'

# Main program starts here:
while True:

    # ALL VALID REQUIREMENTS SET FOR .title() and .upper(). A few extra just for fun have been added.
    # Gather user inputs:
    while True:
        custFirst = input("Enter the customers first name: ").title()
        if custFirst == "":
            print("ERROR - Customer Name cannot be blank.")
        else:
            break

    custLast = input("Enter the customers last name: ").title()
    custAdd = input("Customer Address: ")
    custCity = input("Customer City: ").title()
    
    while True:
        custProv = input("Customer Province (XX): ").upper()
        if custProv not in CAN_PROV:
            print("ERROR - Enter a province in a proper format (XX).")
        else:
            break

    custPostCode = input("Customer Postal Code (A1A 1A1): ").title()
    custPhoneNumber = input("Phone Number (999-999-9999): ")
    
    while True:
        numberInsurCar = int(input("Number of Cars to be insured: "))
        if numberInsurCar < 0:
                print("Please enter a non-negative number.")
        else:
            break
    
    extraLiab = input("Extra Liability up to $1,000,000. (Y/N): ").upper()
    if extraLiab == "Y":
        extraLiab = "Yes"
    else:
        extraLiab = "No"
    
    glassCover = input("Glass Coverage (Y/N): ").upper()
    if glassCover == "Y":
        glassCover = "Yes"
    else:
        glassCover = "No"
    
    loanerCar = input("Would you like a loner car? (Y/N): ").upper()
    if loanerCar == "Y":
        loanerCar = "Yes"
    else:
        loanerCar = "No"

    while True:
        paymentType = input("Enter Payment Type (Full, Monthly, Down Payment): ").title()
        if paymentType not in PAYMENT_TYPE:
            print("ERROR - Enter a valid payment Type.")
        elif paymentType == "Down Payment":
            downPayment = float(input("Enter the down payment: "))
            break
        else:
            break

    # Initialize lists to store claim information
    claim_numbers = [1372, 1723, 1883]
    claim_dates = ["2020-01-08", "2022-04-23", "2023-03-01"]
    claim_amounts = [500.0, 750.0, 1250.0]

    while True:
        previousClaims = input("Would you like to enter any previous claims? (Y/N): ").upper()
        if previousClaims == "Y":
            claimNumber = int(input("Enter Claim Number (XXXX): "))
            claimDate = input("Enter Claim Date (YYYY-MM-DD): ")
            claimDateDSP = datetime.datetime.strptime(claimDate, "%Y-%m-%d")
            claimAmount = float(input("Enter Claim Amount of previous claim: "))
        
            # Add to lists
            claim_numbers.append(claimNumber)
            claim_dates.append(claimDate)
            claim_amounts.append(claimAmount)
            
            Continue = input("Do you want to process another claim (Y/N): ").upper()
            if Continue == "Y":
                claimNumber = int(input("Enter Claim Number (XXXX): "))
                claimDate = input("Enter Claim Date (YYYY-MM-DD): ")
                claimDateDSP = datetime.datetime.strptime(claimDate, "%Y-%m-%d")
                claimAmount = float(input("Enter Claim Amount of previous claim: "))
                # Add to lists
                claim_numbers.append(claimNumber)
                claim_dates.append(claimDate)
                claim_amounts.append(claimAmount)
            elif Continue == "N":
                break
        else:
            break

    # Perform required calculations:
    if numberInsurCar == 1:
        insurancePrem = INSURANCE_PREM_BASE
    else:
        insurancePrem = INSURANCE_PREM_BASE + ((numberInsurCar - 1) * (INSURANCE_PREM_BASE * (1 - ADD_VEHC_DISCOUNT_RATE)))

    extraCost = 0
    if extraLiab == "Yes":
        extraCost += numberInsurCar * CAR_LIABILITY_RATE
    if glassCover == "Yes":
        extraCost += numberInsurCar * GLASS_COVER_RATE
    if loanerCar == "Yes":
        extraCost += numberInsurCar * LOAN_CAR_RATE

    totalInsurPrem = insurancePrem + extraCost
    hST = totalInsurPrem * HST_RATE
    totalCost = totalInsurPrem + hST

    monthlyPayment = (totalCost + PROCESSING_FEE) / 8
    if paymentType == "Down Payment":
        monthlyPayment = ((totalCost - downPayment) + PROCESSING_FEE) / 8

    invoiceDate = CURR_DATE
    firstPaymentDate = first_payment_date

    # Format Displays
    customerName = (f"{custFirst} {custLast}")
    invoiceDateDSP = datetime.datetime.strftime(invoiceDate, "%Y-%m-%d")

    # Display results:
    print("=============================================")
    print(f"{" " * 18}{BOLD}ONE STOP{END}")
    print(f"{" " * 14}{BOLD}INSURANCE COMPANY{END}")
    print("=============================================")
    print(f"{" " * 12}{BOLD}NEW CLAIM INFORMATION{END}")
    print("=============================================")
    print(f"Customer Name:     {customerName:<26s} ")
    print(f"Customer Address:  {address_formatting()}")
    print(f"Phone Number:      {custPhoneNumber:<14s}")
    print("=============================================")
    print(f"Policy Number:                        {POLICY_NUM:>7d}")
    print(f"Number of Insured Cars:                   {numberInsurCar:>3d}")
    print(f"Extra Liability:                          {extraLiab:>3s}")
    print(f"Glass Coverage:                           {glassCover:>3s}")
    print(f"Loaner Car:                               {loanerCar:>3s}")
    print(f"Payment Type:                    {paymentType:>12s}")
    print("=============================================")
    print(f"Insurance Premium:                 {FL.FDollar2(insurancePrem):>10s}")
    print(f"Extra Costs:                       {FL.FDollar2(extraCost):>10s}")
    print(f"Total Insurance Premium:           {FL.FDollar2(totalInsurPrem):>10s}")
    print(f"HST:                               {FL.FDollar2(hST):>10s}")
    print("=============================================")  
    print(f"Total Cost:                        {FL.FDollar2(totalCost):>10s}")
    print(f"Monthly Payment (8 Month Annual):    {FL.FDollar2(monthlyPayment):>8s}")
    print("=============================================")
    print(f"          Invoice Date: {BOLD}{invoiceDateDSP}{END}")
    print(f"       First Payment Date: {BOLD}{first_payment_date()}{END}")
    print("=============================================")
    print()
    print("=============================================")
    print(f"         {BOLD}PREVIOUS CLAIM INFORMATION{END}")
    print()
    print(f"Customer Name:     {customerName:<26s} ")
    print(f"Customer Address:  {address_formatting()}")
    print()
    print(f"{BOLD}{'CLAIM NUMBER':<15}   {'CLAIM DATE':<15}{'CLAIM AMOUNT':<15}{END}")
    print()

    # Print each claim detail under the corresponding header
    for number, date, amount in zip(claim_numbers, claim_dates, claim_amounts):
        print(f"   {number:<15}{date:<15}  {amount:<15.2f}")
    print("=============================================")
    print()
    # Indication for the user that something is happening.
    Message = "Saving Claim Data ..."
    for _ in range(5):  # Change to control no. of 'blinks'
        print(Message, end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)

    # a single line in a file is a record about a single person, place, thing or event.
    # Each record is made up of individual pieces of data know as fields
    #In every record the fields are always in the same order.
    print()
    print("Claim date has been saved")
    print()

    # Save claim information to a file

    f = open('ClaimInformation.dat', 'w')
    for number, date, amount in zip(claim_numbers, claim_dates, claim_amounts):
        f.write(f"{number}, {date}, {amount:.2f}\n")
    f.write(f"{POLICY_NUM}, {customerName}, {numberInsurCar}, {extraLiab}, {glassCover}, {loanerCar}, {paymentType}, {totalInsurPrem}")
    f.close()

    break


# Any housekeeping duties at the end of the program:
# Update any values for the next claim
POLICY_NUM += 1

f = open('Const.dat', 'w')
f.write(f"{POLICY_NUM}\n")
f.write(f"{INSURANCE_PREM_BASE}\n")
f.write(f"{ADD_VEHC_DISCOUNT_RATE}\n")
f.write(f"{CAR_LIABILITY_RATE}\n")
f.write(f"{GLASS_COVER_RATE}\n")
f.write(f"{LOAN_CAR_RATE}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{PROCESSING_FEE}\n")
f.close()


# Any housekeeping duties at the end of the program: