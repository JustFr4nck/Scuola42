import sys
import re

parms = sys.argv

val = 0

if len(parms) == 3:

    key = parms[1]
    text = parms[2]

    content = re.findall(key, text)

    for x in content:

        val += 1

    print(f"Numero di volte che viene ripetuta la parola: {val}")

else:
    print("none")