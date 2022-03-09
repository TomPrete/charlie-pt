def testArgs(*args):
    print(type(args))
    for item in args:
        if item == 'hello':
            print('Do something with value')

employee_1 = {
    'first_name': 'Tom',
    'last_name': 'Prete',
    'title': 'Instructor',
    'salary': 55000
}

def testKwargs(**kwargs):
    print(type(kwargs))
    print(kwargs['first_name'])


# testArgs(1,'random', 'hello', {'one': 'value'}, [5,6,7])
testKwargs(**employee_1) # testKwargs(first_name='Tom', last_name='Prete', title='Instructor')
