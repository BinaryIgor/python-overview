import random
import sys

# either __main__ or name of the script (when imported)
if __name__ == "__main__":
    first_var = 22
    second_var = 'ala'

    print(f'first_var: {first_var}')
    sys.stdout.write(f"second_var: {second_var}\n")

    if_var = 3

    # redundant and, or - just to show syntax
    if if_var == 3 and (True or False):
        print("if var is 3")
    elif if_var >= 0:
        print("if var is at least 0")
        if if_var > 0:
            print("if var is greater than 0")
        else:
            print("if var is 0")
    else:
        print(f"if is: {if_var}")

    print("For loop...")
    # change to range(0, 10, 2) to add step value (1 by default)
    for i in range(0, 10):
        print(i)

        if random.randrange(0, 10) == i:
            print(f"Random same as {i} index, breaking!")
            break

    print("While loop...")
    n = 0
    while n < 10:
        if n == 2:
            print("Skipping 2!")
            n = 4
            continue
        print(n)
        n += 1

    # ternary operator (one line if)
    t = 3
    print(f"Evaluating ternary operator ({t}): {2 if t > 0 else 0}")
