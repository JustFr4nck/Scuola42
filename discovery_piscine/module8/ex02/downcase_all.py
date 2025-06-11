import sys

params = sys.argv

if len(params) == 1:

    print("none")

else:

    for x in params:

        print(str(x).lower())