import sys

params = sys.argv

if len(params) >= 2:

    print(f"Parameters: {len(params) - 1}")

    for x in params[1:]:

        print(f"{x}: {len(x)}")



else:

    print("none")