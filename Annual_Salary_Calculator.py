def Annual_Salary_Calculator(hourly_pay,Vacation_weeks,tax_rate):
#this function calculates the annual salary including unpaid vacation and tax deduction
#this is assuming a 40 hours schedule

    hourly_pay=input("Enter Hourly Salary:")
    hourly_pay = int(hourly_pay)
    Vacation_weeks = input("Enter Unpaid Vacation Weeks: ")
    Vacation_weeks = int(Vacation_weeks)
    tax_rate = input("Enter Tax Rate: ")
    tax_rate = int(tax_rate)
    total=((40)*hourly_pay*(52-Vacation_weeks))-(tax_rate *((40)*hourly_pay*(52-Vacation_weeks))*0.01)
    #print (hourly_pay * Vacation_weeks * tax_rate)
    print("Total Annual salary: ",total)
    return total

Annual_Salary_Calculator(hourly_pay="full-time,40 hours",Vacation_weeks="unpaid vacation weeks",tax_rate = "income tax deduction")

#calling the function