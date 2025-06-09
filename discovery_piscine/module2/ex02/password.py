import time
password = "aurafarming"
n = 0
while n < 3:
    inserisci = input("Inserisci la password: ")

    if password == inserisci:
        print("Accesso garantito")
        break

    else:
        print("Accesso negato")
        n += 1

print("Limite di accesso superato")

time.sleep(10)

print("Riprova ad eseguire il programma")