import time

for x in range(11):

    print(f"Table of {x}:", end =" ")

    for y in range(11):

        result = x * y
        print(f"{result}", end = " ")

    print("\n")