# Calculates new insurance policy information for customers.
# Author: Matt Young
# Date Created: Mar-20-2023

import datetime

# read values from OSICDef.dat
f = open("OSICDef.dat", "r")
policyNum = int(f.readline().strip())
FIRST_PREMIUM = float(f.readline().strip())
ADDITIONAL_PREM_RATE = float(f.readline().strip())
EXTRA_LIABILITY_COST = float(f.readline().strip())
GLASS_COVERAGE_COST = float(f.readline().strip())
LOANER_COST = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
PROCESS_FEE = float(f.readline().strip())
f.close()

PROVINCES = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
extraCosts = 0
invDate = datetime.datetime.today()
year = invDate.year
month = invDate.month
invDate = invDate.strftime("%Y-%m-%d")

month += 1
if month >= 13:
    month -= 12
    year += 1

payDate = f'{year}-{month}-01'
payDate = datetime.datetime.strptime(payDate, "%Y-%m-%d")
payDate = payDate.strftime("%Y-%m-%d")

while True:
    # get inputs from user
    firstName = input("Enter the customer's first name: ").title()
    lastName = input("Enter the customer's last name: ").title()
    address = input("Enter the customer's street address: ").title()
    city = input("Enter the city: ").title()

    while True:
        province = input("Enter the province (XX): ").upper()
        if province in PROVINCES:
            break
        else:
            print('Province must be from list: "AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"')

    postalCode = input("Enter the postal code: ").upper()
    phoneNum = input("Enter the phone number: ")
    numCarsIns = int(input("Enter the number of cars being insured: "))

    while True:
        extraLiability = input("Extra liability up to $1,000,000? (Y/N): ").upper()
        if extraLiability != "Y" and extraLiability != "N":
            print('Please type "Y" or "N".')
        else:
            if extraLiability == "Y":
                extraCosts += EXTRA_LIABILITY_COST
            break

    while True:
        glassCoverage = input("Glass coverage? (Y/N): ").upper()
        if glassCoverage != "Y" and glassCoverage != "N":
            print('Please type "Y" or "N".')
        else:
            if glassCoverage == "Y":
                extraCosts += GLASS_COVERAGE_COST
            break

    while True:
        loaner = input("Loaner car? (Y/N): ").upper()
        if loaner != "Y" and loaner != "N":
            print('Please type "Y" or "N".')
        else:
            if loaner == "Y":
                extraCosts += LOANER_COST
            break

    while True:
        fullMonthly = input('Pay in Full, or in 8 Monthly Payments? (Enter "F" or "M": ').upper()
        if fullMonthly != "F" and fullMonthly != "M":
            print('Please type "F" to pay in full, or "M" for monthly payments.')
        else:
            break

    # Calculate values
    premium = FIRST_PREMIUM + (numCarsIns - 1) * (FIRST_PREMIUM * ADDITIONAL_PREM_RATE)
    subtotal = premium + extraCosts
    hst = subtotal * HST_RATE
    totalCost = subtotal + hst
    monthlyPayment = (totalCost + PROCESS_FEE) / 8

    # Display results to a receipt
    print()
    print("       One Stop Insurance Company")
    print("----------------------------------------")
    print(f'                Invoice Date: {invDate}')
    print(f'                Payment Date: {payDate}')
    print(f'{f"{firstName} {lastName}":<20s} Policy Number: {policyNum}')
    print(f'{address}')
    print(f'{city}, {province}  {postalCode}')
    print(f'{phoneNum}')
    print("----------------------------------------")
    print(f'Premium:                       {f"${premium:,.2f}":>9s}')
    print(f'Extra Costs:                   {f"${extraCosts:,.2f}":>9s}')
    print("                               ---------")
    print(f'Subtotal:                      {f"${subtotal:,.2f}":>9s}')
    print(f'HST:                           {f"${hst:,.2f}":>9s}')
    print("                               ---------")
    print(f'Total Cost:                    {f"${totalCost:,.2f}":>9s}')
    print("----------------------------------------")
    print()

    # Print monthly payment only if user selected the option
    if fullMonthly == "M":
        print(f'Monthly Payment:               {f"${monthlyPayment:,.2f}":>9s}')
    print()

    # save values to file Policies.dat
    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(policyNum)))
    f.write("{}, ".format(str(invDate)))
    f.write("{}, ".format(str(firstName)))
    f.write("{}, ".format(str(lastName)))
    f.write("{}, ".format(str(address)))
    f.write("{}, ".format(str(city)))
    f.write("{}, ".format(str(postalCode)))
    f.write("{}, ".format(str(phoneNum)))
    f.write("{}, ".format(str(numCarsIns)))
    f.write("{}, ".format(str(extraLiability)))
    f.write("{}, ".format(str(glassCoverage)))
    f.write("{}, ".format(str(loaner)))
    f.write("{}, ".format(str(fullMonthly)))
    f.write("{} \n".format(str(f'{totalCost:.2f}')))
    f.close()

    # Increase the policy number for next entry
    policyNum += 1

    while True:
        again = input("Process another claim? (Y/N): ").upper()
        print()
        if again != "Y" and again != "N":
            print('Please type "Y" or "N".')
        else:
            break
    if again == "N":
        break

# write updated values back to OSICDef.dat
f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(policyNum)))
f.write("{}\n".format(str(FIRST_PREMIUM)))
f.write("{}\n".format(str(ADDITIONAL_PREM_RATE)))
f.write("{}\n".format(str(EXTRA_LIABILITY_COST)))
f.write("{}\n".format(str(GLASS_COVERAGE_COST)))
f.write("{}\n".format(str(LOANER_COST)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}".format(str(PROCESS_FEE)))
f.close()

