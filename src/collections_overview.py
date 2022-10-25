numbers_tuple = (1, 2, 3, 4)
numbers_list = [1, 2, 3, 4]
numbers_set = {1, 2, 2, 3, 4}
numbers_map = {'a': 1, 'b': 1, 'b': 2, 'c': 3, 'd': 4}

print(f"Tuple of len ({len(numbers_tuple)}): {numbers_tuple}")
print(f"List of len ({len(numbers_list)}): {numbers_list}")
print(f"Set of len ({len(numbers_set)}): {numbers_set}")
print(f"Map of len ({len(numbers_map)}): {numbers_map}")
print()

print("Iterating over list:")
for v in numbers_list:
    print(v)

print("Iterating over map:")
for k in numbers_map:
    print(f"{k} - {numbers_map[k]}")

# list/collection comprehensions
even_numbers_list = [n for n in numbers_list if n % 2 == 0]
odd_numbers_list = [n for n in numbers_list if n % 2 == 1]
odd_numbers_reversed_list = sorted([n for n in numbers_list if n % 2 == 1], reverse=True)

print(f"Even numbers list: {even_numbers_list}")
print(f"Odd numbers list: {odd_numbers_list}")
print(f"Odd numbers reversed list: {odd_numbers_reversed_list}")

# list mutation
string_list = list()
string_list.append("a")
string_list.append("b")
string_list.extend(["a1", "b2"])
print(f"Mutated string list: {string_list}")
print()

# sublist
print(f"Sublist: {string_list[1: 3]}")
print(f"Reversed sublist: {string_list[2::-1]}")
print()

# map mutation
string_map = dict()
string_map['a'] = 'a-value'
string_map['b'] = 'b-value'
string_map.update({'c': 'c-value', 'd': 'd-value'})
print(f"Mutated string map: {string_map}")
