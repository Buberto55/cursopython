# Dictionaries
# Create
prog_dic = {
    "Bug" : "An error in a program that preveents the program from running as expected.",
    "Function" : "A piece ofr code that you can easly call over an over again",
    "Loop" : "The action of doing something over an over again"
}

print(prog_dic["Function"])
print(prog_dic)

# Edit
prog_dic["Bug"] = "Una pelucita en tu compu"

# Clear
empty_dictionary = {}

prog_dic = {}

print(prog_dic)

for thing in prog_dic:
    print(thing)
    print(prog_dic[thing])

# Exercise 9: Grading program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_scores.items():
    print(key, value)
    if 100 > value > 90:
        student_grades[key] = "Outstanding"
    elif 90 > value > 80:
        student_grades[key] = "Exceeds Expectations"
    elif 80 > value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting
# we can have a dictionary and a list inside a dictionary
travel_log = {
    #"France": ["Paris", "Lille", "Dijon-"],
    #"Germany": ["Stuttgart", "Berlin"]
    "France" : {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5
    },
}

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

print(travel_log["Germany"]["cities_visited"][2])

# Project: The secret audition program instructions
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()

subasta = {}
seguimos = True

print("Bienvenido a la super subasta de bubu!")
print("quien sera capaz de llevarse a este papucho inutil?")
print("\n")

while seguimos:
    nombre = input("Como te llamas? ")
    pago = int(input("Cual es tu subasta: $"))
    subasta[nombre] = pago
    opc = input("Alguien mas va a subastar? si o no? ").lower()
    if opc == "no":
        seguimos = False
        limpiar_pantalla()
    elif opc == "si":
        limpiar_pantalla()
        print("Otra subasta!")
print("El ganador es:",max(subasta,key=subasta.get),
      "Con una subasta de:","$"+str(max(subasta.values())))