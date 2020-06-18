# creating a init method in class
class employee:
    # creating a variable
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = '{}{}@gmail.com'.format(self.name, self.last)

        employee.num_of_emp += 1

# creating another method to call the init property

    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)
# creating a class method

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # using class method as constructor
    @classmethod
    def from_string(cls, emp_str):
        name, last, pay = emp_str.split('-')
        return cls(name, last, pay)


emp_1_str = 'Piyush-Zambad-5000'
emp_2_str = 'Priyanka-Zambad-7000'

new_emp_1 = employee.from_string(emp_1_str)
new_emp_2 = employee.from_string(emp_2_str)


emp_1 = employee('Surbhi', 'Kumat', 1500)
emp_2 = employee('Shashank', 'Kumat', 2000)
# to print number of employees
print(employee.num_of_emp)

print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# changing the value of raise_amount from 1.04 to 1.05
employee.set_raise_amount(1.05)
print(emp_2.fullname())
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

# values for the new employee

print(new_emp_1.fullname())
print(new_emp_1.email)
print(new_emp_1.pay)


print(new_emp_2.fullname())
print(new_emp_2.pay)
