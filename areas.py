import os


def cuadrado():
    n1 = float(input("Primer Lado: "))
    n2 = float(input("Segundo Lado: "))
    resultado= n1 * n2
    print("El Area es: ",resultado)
    


def resrectangulo():
    n1 = float(input("Base: "))
    n2 = float(input("Altura: "))
    resultado= n1* n2
    print("El Area es: ",resultado)


def triangulo():
    n1 = float(input("Base: "))
    n2 = float(input("Altura: "))
    resultado=(n1 * n2) /2
    print("El Area es: ",resultado)


def circulo():
    n1 = float(input("Radio: "))
    resultado= 3.1416*n1*n1
    print("El Area es: ",resultado)


def trapecio():
    n1= float(input("Base mayor: "))
    n2= float(input("Base menor: "))
    n3= float(input("Altura: "))
    resultado= ((n1+n2)*n3)/2
    print("El Area es: ",resultado)


def menu():
    print("1=Cuadrado")
    print("2=Rectanjulo")
    print("3=Trianjulo")
    print("4=Circulo")
    print("5= trapecio")
    print("6= Salir")
    opc = int(input("Elige una opción: "))
    return opc

def menu():
    opcion = 0
    while opcion != 6:
        opcion = menu()
        if opcion == 1:
         cuadrado()
        elif opcion == 2:
            resrectangulo() 
        elif opcion == 3:
            triangulo()
        elif opcion == 4:
            circulo()
        elif opcion == 5:
            trapecio()
        elif opcion == 6:
            print("Fin")
            break
        else:
            print("Opción no válida.")

            input("Presiona Enter para continuar.")
            if os.name == "nt":
                os.system("cls")
                
                
if __name__("__main__"):      
    menu()
   
   
