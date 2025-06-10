import sys
import re

parms = sys.argv

key = "z"

if len(parms) == 2:

    text = parms[1]

    content = re.findall(key, text)

    if key not in text:

        print("none")
        exit

    for x in content:

        print("z", end=" ")

else:
    print("none")
