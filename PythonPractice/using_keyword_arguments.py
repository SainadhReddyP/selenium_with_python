"""
- *args -> from the function calling statement we can pass any number of single values
- **kwargs -> we have to pass any number of key values
"""

def example_args(*args):
    for i in args:
        print(i)


def example_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)


def example_kwargs_two(name, age, location):
    print(name, age, location)


example_args(1,3,5,7,9)
example_kwargs(name='Sainadh', age=28, location='Hyderabad')

input_dict = {'name':'Sainadh', 'age':28, 'location':'Hyderabad'}
example_kwargs_two(**input_dict)
