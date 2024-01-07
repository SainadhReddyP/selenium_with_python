"""
- using *args in function parameters
- sample_fun(*args)
"""


def sample_function(*args):
    for i in args:
        print(i)


def sample_function_two(a,b,c,d):
    print(a,b,c,d)


sample_function(1, 3, 5, 7, 9)
args = [2,4,6,8]
sample_function_two(*args)
