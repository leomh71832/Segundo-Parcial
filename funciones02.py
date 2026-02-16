import os
def suma():
    os.system("cls")
    a=int(input("num1: "))
    b=int(input("num2: "))
    res=a+b
    return res

    print("La suma es: ",res)
    input()
    
    
def resta():
    os.system("cls")
    a=int(input("num1: "))
    b=int(input("num2: "))
    res=a-b
    print("La resta es: ",res)
    input()
    
def menu():
    op=0
    while op!=5:
        print("1.- +\n2- -\n 3.- * \n 4.-/ \n 5.- salir")
        op=int(input("Opcion: "))
        if op ==2:
            resta()



if __name__("_main_"):      
    menu()