# creating a init method in class
import datetime


class employee:
    # creating a variable
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay

        employee.num_of_emp += 1

# creating another method to call the init property
    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.last)

# setting a setter method for fullname to change it at anytime

    @fullname.setter
    def fullname(self, first):
        name, last = first.split(' ')
        self.name = name
        self.last = last

# setting a deleter method to delete the fullname we alloted

    @fullname.deleter
    def fullname(self):
        print('Delete name!!')
        self.name = None
        self.last = None

# added property decorator to operate email address whenever we change values outside the boundary
    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.name, self.last)

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)


# Magic/Dunder Method to print the content of classes


    def __repr__(self):
        return "employee('{}','{}',{})".format(self.name, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
# creating a class method

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # using class method as constructor
    @classmethod
    def from_string(cls, emp_str):
        name, last, pay = emp_str.split('-')
        return cls(name, last, pay)

    # creating static method to determine whether it is working day or not

    @staticmethod
    def working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# creating a new class developer under class employee which can inherit all the properties of its parent class


class developer(employee):
    # to add more arguments in developer class we have to create init method again

    def __init__(self, name, last, pay, prog_lang):
        # inherit the properties of employee class into developer without repeating the existing properties of employee class
        # we can use employee.__init__(name,last,pay) here as well
        super().__init__(name, last, pay)
        self.prog_lang = prog_lang

<<<<<<< HEAD
# magic method to add pay of two developers
    def __add__(self, other):
        return self.pay + other.pay

=======
>>>>>>> Inherited_class
# creating another new class manager


class manager(employee):
    def __init__(self, name, last, pay, employees=None):
        super().__init__(name, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
<<<<<<< HEAD
            print('-->', emp.fullname)
=======
            print('-->', emp.fullname())
>>>>>>> Inherited_class


my_date = datetime.date(2020, 6, 17)

print(employee.working_day(my_date))

emp_1_str = 'Piyush-Zambad-5000'
emp_2_str = 'Priyanka-Zambad-7000'

new_emp_1 = employee.from_string(emp_1_str)
new_emp_2 = employee.from_string(emp_2_str)


emp_1 = employee('Surbhi', 'Kumat', 1500)
emp_2 = employee('Shashank', 'Kumat', 2000)
# to print number of employees
print(employee.num_of_emp)
print(emp_1.fullname)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# changing the value of raise_amount from 1.04 to 1.05
employee.set_raise_amount(1.05)
print(emp_2.fullname)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

# values for the new employee
# implemented name change by property decorator
new_emp_1.fullname = 'Keshav Singh'
print(new_emp_1.fullname)
print(new_emp_1.email)
print(new_emp_1.pay)
# deleting the new_emp_1 fullname from deleter method
del new_emp_1.fullname


print(new_emp_2.fullname)
print(new_emp_2.pay)

# inheriting all the properties from parent class and printing values for new class developer

dev_1 = developer('Aarushi', 'Chajjed', 3000, 'Python')
dev_2 = developer('Khushi', 'Chajjed', 11000, 'Java')

<<<<<<< HEAD
print(dev_1.fullname)
=======
print(dev_1.fullname())
>>>>>>> Inherited_class
print(dev_1.email)
print(dev_1.prog_lang)

# inheriting the properties from employee class

mgr_1 = manager('Kavya', 'Sharma', 5000, [dev_1])
# adding the functions for adding and removing employees
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(mgr_1.email)
mgr_1.print_emp()
<<<<<<< HEAD

# to check whether a variable is instance of class isinstance() is used

print(isinstance(dev_1, developer))
print(isinstance(dev_1, manager))

# to check whether a class is subclass of class issubclass() is used

print(issubclass(developer, employee))
print(issubclass(developer, manager))

# here it was giving an object as output but after using magic methods it changes its output
print(emp_1)
print(dev_1+dev_2)
=======
>>>>>>> Inherited_class
