import math

x = 3
y = 2

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} ** {y} = {x ** y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")
print()

# increase/decrease by 1
x += 1
y -= 1
print(f"increased by 1 x: {x}, decreased by 1 y: {y}")
print()

d_num = 2.6
print(f'floor({d_num}): {math.floor(d_num)}')
print(f'ceil({d_num}): {math.ceil(d_num)}')
print(f'round({d_num}): {round(d_num)}')
