import os


def suma():
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    return n1 + n2

def resta():
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    return n1 - n2

def multiplicacion():
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    return n1 * n2

def dividir():
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    if n2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    return n1 / n2

def menu():
    print("1= SUMA")
    print("2= RESTA")
    print("3= MILTIPLICACION")
    print("4= DIVICION")
    print("5= Salir")
    opc = int(input("Elige una opción: "))
    return opc


opcion = 0
while opcion != 5:
    opcion = menu()
    if opcion == 1:
        resultado = suma()
        print("El resultado es: ",resultado)
    elif opcion == 2:
        resultado = resta()
        print("El resultado es: ",resultado)
    elif opcion == 3:
        resultado = multiplicacion()
        print("El resultado es: ",resultado)
    elif opcion == 4:
        resultado = dividir()
        print("El resultado es: ",resultado)
    elif opcion == 5:
        print("Fin")
        break
    else:
        print("Opción no válida.")

    input("Presiona Enter para continuar.")
    if os.name == "nt":
        os.system("cls")
   