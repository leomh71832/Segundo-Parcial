
'''
Docstring for 08-funciones
las funciones en py son bloques de codigo reutilizable que realizan una tarea en especifico,
sirven para reutilizar, orfanizar y hacer mas claro del codigo

para que sirven:
Evitan repetir codigo
permite dividir en problema grande en partes pequenas
hacen el programa mas facil de mantener
mejora la legibilidad


EN PY SE FEFINEN CON -> def:
def nombre_funcion (parametros):
|   #bloque de codigo
|   return valor
'''

def nombre():#funcion que no recive nada ni regresa nada 
    print("Hola Mundo!!")
    
nombre()

def suma():
    a=6
    b=7
    c=a+b
    
    a=3
    b=7
    c=a+b
    return c


print(suma())

def multiplica(a,b):
    return a*b

print("La multiplicacion es: ",multiplica(6,7))