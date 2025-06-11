
def greetings(name):

    if str(name).isdigit():
        print("ERROR: it was not a name!")

    elif str(name) != "":
        print(f"Hello, {name}")
    
    else:
        print("Hello, noble stranger!")


greetings("Alexandra")
greetings("Wil")
greetings("")
greetings("42")