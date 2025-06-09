
n = ""

while True:

    try:
        n = int(input("Inserire un numero da verificare: "))
        break

    except ValueError:
        print("Inseriere un valore numerico")
    

if n < 0:
    print("Il numero e' negativo")

elif n > 0:
    print("Il numero e' positivo")

else:
    print("Il numero e' uguale a 0")
