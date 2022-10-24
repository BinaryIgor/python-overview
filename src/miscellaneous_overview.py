some_tuple = (4, 5)
a, b = some_tuple
print(f"Destructured {some_tuple} tuple: {a}, {b}")

some_map = {'a': 2, "b": 3}

print(f"Destructuring {some_map} map...")
for k, v in some_map.items():
    print(f'{k}: {v}')
