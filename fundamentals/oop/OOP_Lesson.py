# class User:
#     def log(self):
#         print(self)


# class Customer:
#     (User)

#     def __init__(self, name, membership_type):
#         self.name = name
#         self.membership_type = membership_type

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         self._name = name

#     def update_membership(self, new_membership):
#         print("Calculating costs...")
#         self.membership_type = new_membership

#     def read_customer():  # static Method, invoked on the Class itself and not any OBJECT/Instance
#         print("Reading customer from DB")

#     def __str__(self):  # returns a string representaion of the OBJECT
#         print("Converting to a String")
#         return self.name + " " + self.membership_type

#     def print_all_customers(customers):
#         for customer in customers:
#             print(customer)

#     __hash__ = None

#     __repr__ = __str__

#     def __eq__(self, other):  # used to compare OBJECTS
#         if self.name == other.name and self.membership_type == other.membership_type:
#             return True
#         return False


# # customer1 = Customer("Nick", "Gold")
# # customer2 = Customer("John", "Bronze")  # this can be a list
# customers = [Customer("Nick", "Gold"), Customer("John", "Bronze")]

# # how to access customer and their #attributes
# # print(customers[1].membership_type)


# # customers[1].update_membership("Platimun")

# # print(customers[1])

# # Customer.read_customer()

# # Customer.print_all_customers(customers)

# print(customers)


#OOP Inheritance###################################

class Employee:
    """A class for an employee's information"""
    bonus = 10000
    total_employees = 0

    def __init__(self, name, emp_num, salary):
        self.name = name
        self.emp_num = emp_num
        self.salary = salary
        Employee.total_employees += 1

    def get_employee_info(self):
        return 'Employee: ' + self.name + '\n' \
            'Emp #: ' + str(self.emp_num) + '\n'

    def add_bonus_to_salary(self):
        salary_bonus = int(self.salary + self.bonus)
        return ' Employee Name: ' + self.name + '\n' \
            ' Salary + Bonus: ' + str(salary_bonus) + '\n'


class Developer(Employee):
    def __init__(self, name, emp_num, salary, lang):
        self.lang = lang
        super().__init__(name, emp_num, salary)


class Tester(Employee):
    def __init__(self, name, emp_num, salary, web_mobile):
        self.web_mobile = web_mobile
        Employee.__init__(self, name, emp_num, salary)


emp1 = Developer('Developer John', 1, 120000, 'Python')
emp2 = Employee('Employee Jane', 2, 110000)
emp3 = Tester('Tester James', 3, 100000, 'Web')

print('Employee 1 Is A', emp1.lang, 'Developer')
print(emp1.add_bonus_to_salary())
print('Employee 3 Is A', emp3.web_mobile, 'Tester')
print(emp2.add_bonus_to_salary())
