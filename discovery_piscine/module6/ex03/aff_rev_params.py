import sys

parm = sys.argv

if len(parm) < 3:

    print("none")

else:
    
    for x in reversed(parm):

        print(x)