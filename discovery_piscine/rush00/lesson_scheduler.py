import re
import time

f = open("schedule.txt", "a")


#Controllo se i dati inseriti sono stringhe
def insert_text(x):


    if x.isalpha():
        return x

    print("ERRORE: Inserire nome senza numeri")
    return -1



#Creazione richiesta dati testo
def create_request(request):
    
    while True:

        x = str(input(request))

        if insert_text(x) != -1:
        
            break
    
    return x



#Creazione richiesta orario
def inser_hour(request):
    
    while True:

        x = str(input(request))

        if controllaOrario(x) != -1:
        
            break
    
    return x



#Creazione richichiesta durata
def inser_durata(request):
    while True:

        x = str(input(request))

        if controllaDurata(x) != -1:
        
            break
    
    return x



#Controllo orario
def controllaOrario(x):

    if re.match(r"^\d{1,2}:\d{2}-\d{1,2}:\d{2}$", x):
        return x
    
    else:

        print("ERRORE: Formato orario non valido")
        return -1



#Controllo corretteza durata
def controllaDurata(x):

    if str(x).isdigit() and int(x) > 0:
        return x
    else:
        print("ERRORE: Formato durata non valido")
        return -1


# Inserimento nel dizionario 'schedule'
def insert_activity(schedule, materia, giorno, attivita, orario, durata):
    if giorno not in schedule['attività']:
        schedule['attività'][giorno] = []

    # Aggiungi la nuova attività
    schedule['attività'][giorno].append({
    'materia': materia,
    'tipo': attivita,
    'orario': orario,
    'durata': durata
    })
    return schedule

#calcolo ore 
def calcoloOre(schedule):
    allDurations = {}

    for attivita_list in schedule['attività'].values():
        for giorni in attivita_list:
            attivita = giorni['tipo'] 
            
            if attivita in allDurations:
                #Se giorni esiste nello schedule
                allDurations[attivita] += int(giorni['durata'])
            else:
                #Se giorni non esiste nelo schedule
                allDurations[attivita] = int(giorni['durata'])

    return allDurations

        

# Salva il dizionario nel file
def save_schedule(schedule):
    with open("schedule.txt", "w") as f:
        f.write(str(schedule))

# Carica il file schedule.txt se esiste e contiene dati validi
def load_schedule():

    try:
        with open("schedule.txt", "r") as f:
            content = f.read()
            if content.strip():
                return eval(content)
    except:
        pass
    return None

#___MAIN___
class main():

    schedule = load_schedule()

    if not schedule:
        nome_prof = create_request("Inserire nome del professore: ")
        schedule = {
            "professore": nome_prof,
            "attività": {}
        }
    else:
        print(f"Benvenuto di nuovo, professore {schedule['professore']}!")
 

    #Requests
    materia_req = "Inserire materia: "
    giorno_req = "Inserire giorno della settimana: "
    attivita_req = "Inserire attivita': "
    orario_req = "Inserire orario: "
    durata_req = "Inserire durata (in ore): "
    
    while True:

        #Inserimento dati richiesti
        materia = create_request(materia_req)
        giorno = create_request(giorno_req)
        attivita = create_request(attivita_req)
        orario = inser_hour(orario_req)
        durata = inser_durata(durata_req)
        schedule = insert_activity(schedule, materia, giorno, attivita, orario, durata)

        close = str(input("Continuare ad inserire?(Inserire: CLOSE per concludere l'inserimento): "))

        save_schedule(schedule)

        if close == "CLOSE":
            break

      
    #Stampa corretta sul terminale
    print("Ecco il tuo programma settimanale:")
    print("-" * 30)
    print(f"===== Orario di lezione di {schedule['professore']} =====")
    for giorno, attivita in schedule['attività'].items():
        print(f"{giorno}:")
        for att in attivita:
            print(f"-{att['tipo']}-  {att['materia']} - ({att['orario']}) \n")

    print("=" * 30)
    
    for attivita, ore in calcoloOre(schedule).items():
        print(f"Ore totali di {attivita}: {ore} ore")

    print("=" * 30)

    print("ATTIVITA' SALVATE IN schedule.txt")

    print("-" * 30)

#___CHIUSURA MAIN___



