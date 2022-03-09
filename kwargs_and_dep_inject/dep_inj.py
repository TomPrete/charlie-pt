# Tightly Coupled
def make_api_call_write_to_file(url, ):
    import http_request, file_writer # made up
    result = http_request.get(url)
    data = result.to_str()
    file_obj = file_writer.write(data)
    file_obj.close()

from http_request import HttpRequest
from requests import Request
# Decoupled <- Dependency Injection
def make_api_call_write_to_file(url, http_request, file_writer):
    result = http_request.get(url)
    data = result.to_str()
    file_obj = file_writer.write(data)
    file_obj.close()

make_api_call_write_to_file('www.somethign.com', Request, Writer)
make_api_call_write_to_file('www.somethign.com', HttpRequest, FileWriter)

# Tightly Coupled
class Oak:

    def __init__(self):
        self.branch = Branch()

# Dependency Injection

class Branch:
    pass

class OtherBranch:
    pass

class Oak:

    def __init__(self, branch):
        self.branch = branch

oak_1 = Oak(Branch())
oak_1 = Oak(OtherBranch())

class Tree:

    def __init__(self, bearers_fruit=True):
        self.bearers_fruit = bearers_fruit
        self.fruit = []

    # Coupled
    def add_fruit_to_tree(self):
        self.fruit.append(Apple())

    # Dependency Injection
    def add_fruit_to_tree(self, fruit_instance):
        self.fruit.append(fruit_instance)
