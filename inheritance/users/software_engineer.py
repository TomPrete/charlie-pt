from users.employee import Employee

class SoftwareEngineer(Employee):

    def __init__(self, first_name, last_name, employee_id, title, language):
        super().__init__(first_name, last_name, employee_id, title)
        self.language = language

    def tell_me_about_yourself(self):
        return f"My name is {self.first_name} {self.last_name} and I'm a {self.title} and my primary coding language is {self.language}."

