
while True:
    try:
        first = int(input("Inserisci il primo valore: "))
        second = int(input("Inserisci il secondo valore: "))
        break

    except ValueError:
        print("Inserisci valori numerici")

result = first * second

print(f"{first} X {second} = {result}")

if result > 0:
    print("il numero e' positivo")

elif result < 0:
    print("il numero e' negativo")
    
else:
    print("Il numero e' uguale a 0")