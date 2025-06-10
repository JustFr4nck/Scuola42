import sys

parms = sys.argv

text = ""

if len(parms) >= 2:

    for x in parms:

        text = str(x + "ism")
        print(text)

else:
    print("none")
