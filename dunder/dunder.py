class MyClass:

    def __init__(self):
        print("__INIT__ ran")
        self.data = 4

    def __new__(cls, *arg, **kwargs):
        print('__NEW__ ran')
        return super().__new__(cls, *arg, **kwargs)

    def __del__(self):
        print("__del__ ran")

    def __str__(self):
        print("__STR__ ran")
        return f"This is a string representation of the instance of the object: {self.data}"

    def __repr__(self):
        print("__REPR__ ran")
        return f"some other representation of the object"

hello = MyClass()
print(dir(hello))

