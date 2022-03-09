from users.employee import Employee

class ProductManager(Employee):

    def __init__(self, first_name, last_name, employee_id, title, certification):
        super().__init__(first_name, last_name, employee_id, title)
        self.certification = certification


    def tell_my_about_yourself(self):
        return f"My name is {self.first_name} and I'm a {self.title}. I hold {self.certification} certification."


    def say_hello(self):
        return 'Hi! How are you?'
