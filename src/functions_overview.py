def add(a, b):
    return a + b


def nested_add(a, b):
    def add(a, b):
        print("calling nested add!")
        return a + b

    return add(a, b)


def add_function(a, b):
    return lambda: add(a, b)


def default_arg_func(a, b=None):
    print(f"Calling default arg function.. {a}, {b}")


def variable_args_func(*args):
    print(f"Variable args function: {args}")


def variable_kwargs_func(**kwargs):
    print(f"Variable kw args function: {kwargs}")


a = 3
b = 4

print(add(a, b))
print(nested_add(a, b))

default_arg_func(a)
default_arg_func(a=11, b=4)

print("....")
variable_args_func()
variable_args_func(2)
variable_args_func(2, 3)
variable_args_func(*[2, 3])

print("....")
variable_kwargs_func()
variable_kwargs_func(a=b, z='z argument')
variable_kwargs_func(**{'b': 4, 'c': 4})

print('...')

func_var = add
print(func_var(2, 3))

closed_add = add_function(2, 3)
print(closed_add())

lambda_var = lambda a, b: a + b
print(lambda_var(2, 3))
