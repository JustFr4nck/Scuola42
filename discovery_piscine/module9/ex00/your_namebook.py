

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}



def array_of_names(persons):

    ar = [] 

    for x,y in persons.items():
        
        item = str(x) + " " + str(y)

        ar.append(item)
    
    return ar

print(array_of_names(persons))