import sys

params = sys.argv

if len(params) == 2:

    user = input("What was the parameter? : ")

    if params[1] == user:
        print("Good Job!!!")

    else:
        print("Nope, sorry...")
else:

    print("none")