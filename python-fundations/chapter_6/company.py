from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee
# lowercase: file name
# uppercase: class name

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('---------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Payback for:', i.fname, i.lname)
            print(f'Amount:  ${i.calculate_paycheck():,.2f}')
            print('---------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Martina', 'Balestrin', 250000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Júlia', 'Giumbelli', 25, 200)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee('Seulgi', 'Kang', 185000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()