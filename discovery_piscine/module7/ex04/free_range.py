import sys

params = sys.argv[1:]




if len(params) == 2:


    try:
        first = int(params[0])
        second = int(params[1])

        if first > second:

            first, second = second, first

        for x in range(first, second + 1):
            print(x)

    except ValueError:
        print("ERRORE: Inserire valore numerico")
    

else:
    print("none")
