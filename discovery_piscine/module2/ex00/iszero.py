
n = ""

while n.isdigit() == False:

    n = input("Inserire un numero da verificare: ")

    if n.isdigit() == False:
        print("ERRORE: Inserire un valore numerico")

n = int(n)

if n == 0:
    print("Il numero e' uguale a 0")
else:
    print("Il numero e' diverso da 0")