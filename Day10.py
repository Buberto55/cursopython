# Functions with outputs
import string

def format_name(fname, lname):
    """Take a first and last name and format it to return 
    the title case version of the name"""
    # More than one return value
    if fname == "" or lname == "":
        return print("Dato invalido")
    
    Cfname = fname.title()
    Clname = lname.title()
    return(f"{Cfname} {Clname}")

print(format_name("JANNU","herrera"))

# Exercise 10 leap year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

print(leap_year(2100))

# Project calculator

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

op = {"+": add,
      "-": sub,
      "*": mul,
      "/": div
      }

print("Echale numeros!!!!")
stay = True
con = True
acu = 0
while stay:
    con = True
    a = float(input("Escribe el primer numero: "))
    o = str(input("Selecciona la operacion '+', '-', '*', '/': "))
    b = float(input("Escribe el segundo numero: "))
    acu = op[o](a,b)
    print(f"{a} {o} {b} = {acu}")
    
    while con:
        sig = input(f"Escribe 'c' si quieres seguir operando con {acu} o escribe 'n' si quieres comenzar de nuevo: ")
        if  sig == "c":
            a = acu
            o = str(input("Selecciona la operacion '+', '-', '*', '/': "))
            b = float(input("Escribe el segundo numero: "))
            acu = op[o](a,b)
            print(f"{a} {o} {b} = {acu}")
        elif sig == "n":
            con = False
            acu = 0
        else:
            print("Sin calculadora por payaso")
            con = False
            stay = False