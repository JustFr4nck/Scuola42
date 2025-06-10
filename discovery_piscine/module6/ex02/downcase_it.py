import sys

param = sys.argv

if len(param) == 2:
    print(str(param[1].lower()))

else:
    print("none")