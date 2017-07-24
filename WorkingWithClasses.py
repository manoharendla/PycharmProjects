import traceback


class Employee:
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count += 1
    def getEmployeeName(self):
        print "Employee name is:", self.name

    def getEmployeeSalary(self):
        print "Salary of Employee:", self.name, "is", self.salary

    def calculateSalaryDifference(self):
        manuSalary= int(raw_input("Please enter Manu Salary"))
        moniSalary= int(raw_input("Please enter Moni salary"))
        try:
            print "Calculating the salary difference"
            salaryDifference=moniSalary-manuSalary
            if salaryDifference < manuSalary:
                raise ValueError
        except ValueError,err:
            traceback.print_stack()





emp1 = Employee("Mano",2000)
emp2 = Employee ("Moni",3000)

emp1.getEmployeeName()
emp1.getEmployeeSalary()

emp2.getEmployeeName()
emp2.getEmployeeSalary()
emp1.calculateSalaryDifference()




