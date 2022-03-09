class Employee:
    num_of_employees = 0

    def __init__(self, first_name, last_name, employee_id, title):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.title = title
        Employee.num_of_employees += 1


    def tell_me_about_yourself(self):
        return f"Hi my name is {self.first_name} {self.last_name} and I'm a {self.title}."

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee_id}"

    def say_hello(self):
        return 'Hello!'
