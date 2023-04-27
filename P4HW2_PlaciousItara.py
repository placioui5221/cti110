#Comments up here

def main():
    overTime = 0
    overTimePay = 0
    numEmployees = 0
    totOverTimePay = 0
    totRegPay = 0
    totGrossPay = 0
    name = input("Enter employee's name or " + 'Done' + "to terminate:")
    while name !="Done":
        #name = input("Enter employee's name or " + 'Done' + "to terminate: ")
        hours = float(input("How many hours did " + name + " work? "))
        payRate = float(input("What is " + name + "s pay rate:"))
        #calculate your pay and overtime pay then display

        if hours > 40: 
            regPay = 40 * payRate
            overTime = hours - 40
            overTimePay = overTime * 1.5 * payRate
            grossPay = regPay + overTimePay
        else:
            regPay = hours * payRate
            grossPay = regPay
        print("Employee Name: " + name)
        print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
        print(hours, payRate, overTime, overTimePay, regPay, grossPay)
            
        numEmployees = numEmployees + 1
        totOverTimePay = overTimePay + totOverTimePay
        totRegPay = totRegPay + regPay
        totGrossPay = totGrossPay + grossPay
        #print each employee
        print()
        name = input("Enter employee's name or " + 'Done' + "to terminate: ")
    print("Total number of employees entered: ",numEmployees)
    print("Total amount paid for overtime" ,totOverTimePay)
    print("Total amount paid for reghours" ,totRegPay)
    print("Total amount paid in gross" ,totGrossPay)
    print()
    print("Program has terminated")

main()
