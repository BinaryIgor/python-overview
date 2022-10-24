import os

some_tuple = (4, 5)
a, b = some_tuple
print(f"Destructured {some_tuple} tuple: {a}, {b}")

some_map = {'a': 2, "b": 3}

print(f"Destructuring {some_map} map...")
for k, v in some_map.items():
    print(f'{k}: {v}')

print()
print(f"All env variables:")
for k in os.environ.keys():
    print(k)

print()
print(f'PATH env variable: {os.environ["PATH"]}')
