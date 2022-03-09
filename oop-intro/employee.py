class Employee:
    num_of_employees = 0
    annual_raise_percentage = 1.03
    all_posts = ['user 1 post', 'user 2 post', 'etc']

    def __init__(self, employee_info):
        self.first_name = employee_info['first_name']
        self.last_name = employee_info['last_name']
        self.title = employee_info['title']
        self.salary = employee_info['salary']
        self.email = f"{employee_info['first_name'].lower()}.{employee_info['last_name'].lower()}@email.com"

        Employee.num_of_employees += 1

    # Instance Methods because they refer to the intance of the class
    def say_hello(self):
        return f"Hello my name is {self.first_name} and I'm an {self.title}."

    # Instance Methods because they refer to the intance of the class
    def give_raise(self, bonus=0):
        self.salary = int((self.salary * Employee.annual_raise_percentage) + bonus)
        return self.salary

    @classmethod
    def set_raise_amount(cls, amount):
        print(cls)
        cls.annual_raise_percentage = amount

    @staticmethod
    def check_federal_tax_bracket(salary):
        if salary <= 9950:
            return '10%'
        elif salary <= 40525:
            return '12%'
        elif salary <= 86375:
            return '22%'
        elif salary <= 164925:
            return '24%'
        elif salary <= 209425:
            return '32%'
        elif salary <= 523600:
            return '35%'
        else:
            return '37%'


employee_1 = {
    'first_name': 'Tom',
    'last_name': 'Prete',
    'title': 'Instructor',
    'salary': 55000
}

emp_1 = Employee({
    'first_name': 'Tom',
    'last_name': 'Prete',
    'title': 'Instructor',
    'salary': 55000
})
# emp_2 = Employee('Jon', 'Young', 'Director of Education', 65000)
print(emp_1.say_hello())
print(emp_1.give_raise(2000))
Employee.set_raise_amount(1.07)
print(Employee.check_federal_tax_bracket(50000))
