import os
os.system("cls")
alumnos= []
while True:
    try:
        num=int(input("Ingrese la cantidad de alumnos: "))
        break #si la conversion es exitosa salimos del bucle
    except ValueError:
        print("Error: Ingresa un numero")

for i in range(num):
    nombre = input ("Ingrese el nombre del alumno: ")
    edad = int(input( "Ingrese la edad del alumno: "))
    materia = input( "Ingrese la materia del alumno: ")
    calificacion = float (input("Ingrese la calificacion del alumno: "))
    alumno = {
    "nombre": nombre,
    "edad": edad,
    "materia": materia,
    "calificacion": calificacion
    }
    alumnos.append(alumno)
    #mostrar la cantidad de alumnos ingresados
if alumnos:
    total_calificaciones = sum(alumno["calificacion"] for alumno in alumnos)
    promedio = total_calificaciones / len( alumnos)
    print (f"Promedio de calificaciones: {promedio}")

else:
    print("NO SE INGRESARON CALIFICACIONES")


print("La lista completa de alumnos:")#muestra la lista completa

