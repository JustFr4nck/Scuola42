import sys

params = sys.argv[1:]

#METODI
def shrink(x):

    return x[:8]

        
def enlarge(x):

    while True:

        if len(x) != 8:

            x += "z"
        else:
            break
    
    return x

#MAIN

if len(params) < 1:

    print("none")

else:

    for x in params:

        if len(x) >= 8:

            print(shrink(x))

        
        else:
            print(enlarge(x))


