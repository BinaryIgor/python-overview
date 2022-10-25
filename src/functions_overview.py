def add(a, b):
    print(f"Calling add ({a}, {b})!")
    return a + b


def nested_add(a, b):
    def add(a, b):
        print(f"Calling nested add ({a}, {b})!")
        return a + b

    return add(a, b)


def add_function(a, b):
    return lambda: a + b


def default_arg_function(a, b=None):
    print(f"Calling default arg function.. {a}, {b}")


def variable_args_function(*args):
    print(f"Variable args function: {args}")


def variable_kwargs_function(**kwargs):
    print(f"Variable kw args function: {kwargs}")


a = 3
b = 4

print(add(a, b))
print(nested_add(a, b))

default_arg_function(a)
default_arg_function(b=4, a=11)

print("....")

variable_args_function()
variable_args_function(2)
variable_args_function(2, "two")
variable_args_function([2, "three"])
variable_args_function(*[2, "three"])

print("....")
variable_kwargs_function()
variable_kwargs_function(a=b, z='z argument')
variable_kwargs_function(**{'b': 4, 'c': 4})

print('...')

func_var = add
print(func_var(2, 3))

closed_add = add_function(2, 3)
print(closed_add())

lambda_var = lambda a, b: a + b
print(lambda_var(2, 3))
